

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.conf import settings
from django.utils.text import slugify

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
            .filter(status='published')

class ContentBase(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')

    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')


    @property
    def displayName(self):
        return self.__str__()

    def __str__(self):
        return ''.join([self.firstName , ', ', self.lastName])

    class Meta:
        abstract = True

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def __str__(self):
        return self.title


class Post(ContentBase):

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        def addHighlight(s):
            if "ਅੰਗ" in s or "Raag" in s : return ""
            if "||" in s : return "*" + s + "*"
            return "**" + s + "**" if ("॥" in s and not "**" in s) else s

        #super(PostAdmin, self).save_model(request, obj, form, change)

        lines = self.body.splitlines()
        new_list = [addHighlight(i) for i in lines ]
        self.body = "\n".join(line.strip() for line in new_list)


        super(Post, self).save(*args, **kwargs)

    explanation = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=250,blank=True, null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               blank=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='posts_liked',
                                        blank=True)

    tags = TaggableManager(blank=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    class Meta:
        ordering = ('-publish',)


class Article(ContentBase):

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_articles',
                               blank=True)

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('blog:article_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    class Meta:
        ordering = ('-publish',)


class Shabad(ContentBase):

    link = models.FileField()

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_shabads',
                               blank=True)

    def get_absolute_url(self):
        return reverse('blog:shabad_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    class Meta:
        ordering = ('-publish',)



class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_comments',)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)