from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):  # or StackedInline
    model = Comment
    extra = 1  # show one empty form by default
    fields = ('author', 'text', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    inlines = [CommentInline]  # 👈 allows managing comments inside a post


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at')
    search_fields = ('author', 'text')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)
