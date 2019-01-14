from django.contrib import admin

# Register your models here.

from .models import *

class MyAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    fields = ('title', 'slug', 'body', 'explanation', 'tags', 'status', 'link',)

    def save_model(self, request, obj, form, change):
        def addHighlight(s):
            if "ਅੰਗ" in s or "Raag" in s : return ""
            if "||" in s : return "*" + s + "*"
            return "**" + s + "**" if ("॥" in s and not "**" in s) else s

        print(request.user)
        #if not obj.author.id:
        obj.author = request.user
        lines = obj.body.splitlines()
        new_list = [addHighlight(i) for i in lines ]

        obj.body = "\n".join(line.strip() for line in new_list)

        print(obj.body)
        #obj.last_modified_by = request.user
        obj.save()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author',  'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author' ,'body')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()