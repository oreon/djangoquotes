

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.conf import settings
from django.utils.text import slugify

from textblob import TextBlob

# import nltk
# nltk.download('brown')



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

numbersDict = {"੧":'1', "੨": "2" , "੩": "3" ,"੨": "2" , "੪": "4"  ,  "੫" : "5", "੬": "6",
               "੭": "7" , "੮": "4"  ,  "੯" : "5", "੦": "0"}


def  findPage(s):
    lines = s.splitlines()
    for s in lines:
        if "ਅੰਗ" in s or "Raag" in s:
            l = s.split()
            page = l[l.index('ਅੰਗ') + 1]
            trsPage = [numbersDict.get(p) for p in page]
            return int(''.join(trsPage))

def findInfo(s): return next( (x for x in s.splitlines() if x.startswith("Raag")) , "")

def findTags(s):
    phrases =  TextBlob(s).noun_phrases
    return phrases

def addHighlight(s):
    if "ਅੰਗ" in s or "Raag" in s:
        return ""
    if "||" in s : return "*" + s + "*"
    return "**" + s + "**" if ("॥" in s and not "**" in s) else s

LNK_URL = "https://www.searchgurbani.com/guru-granth-sahib/ang/"

class Post(ContentBase):

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if not self.page:
            self.page = findPage(self.body)
        self.info = findInfo(self.body)

        new_list = [addHighlight(i) for i in self.body.splitlines() ]
        self.body = "\n".join(line.strip() for line in new_list)

        super(Post, self).save(*args, **kwargs)

        if not self.tags:
            self.tags = findTags(self.body)


    explanation = models.TextField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               blank=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='posts_liked',
                                        blank=True)

    info = models.CharField(max_length=250, blank=True)

    tags = TaggableManager(blank=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def get_link(self):
        return LNK_URL + str(self.page) if self.page else ""

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