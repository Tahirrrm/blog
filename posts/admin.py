from django.contrib import admin
from .models import Comment, Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =("title","author","created_at")
    list_filter =("created_at","author")
    search_filter =("title", "text")
    filter_horizontal =("favorites",)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =("post", "author","created_at")
    list_filter = ("created_at", "author")
    search_filter = ("text",)


    