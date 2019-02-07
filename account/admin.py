from django.contrib import admin
from .models import Profile
from django.utils.html import format_html

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'city', 'gender' , 'age', 'image_tag']
    readonly_fields = ['image_tag', 'age']
    search_fields = ['user__username', 'city']
    #list_filter = ( 'created',  'user')

    def image_tag(self, obj):
        print(obj.photo.url)
        return format_html('<img src="{}" width="200" height="200" />'.format(obj.photo.url))

    image_tag.short_description = 'Image'

