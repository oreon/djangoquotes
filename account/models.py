from django.db import models
from django.conf import settings
from datetime import datetime


class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=10,
                            choices=GENDER_CHOICES, blank=True, null=True)
    city=models.CharField(max_length=250,blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    @property
    def age(self):
        return int((datetime.now().date() - self.date_of_birth).days / 365.25)

    # def image_tag(self):
    #     return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.image))
    #
    # image_tag.short_description = 'Image'

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
