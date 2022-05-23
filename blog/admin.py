from django.contrib import admin
from .models import Post, Community, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'community', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('created_on',)
    summernote_fields = ('body')

@admin.register(Community)
class CommuityAdmin(admin.ModelAdmin):

    list_display = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'created_on', 'post', 'body')
