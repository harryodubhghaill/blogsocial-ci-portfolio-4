from django.contrib import admin
from .models import Post, Community, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')

admin.site.register(Community)

admin.site.register(Comment)
