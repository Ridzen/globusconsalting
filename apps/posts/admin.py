from django.contrib import admin

from apps.posts.models import Post, PostCategories


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    pass


@admin.register(PostCategories)
class AdminProductCategory(admin.ModelAdmin):
    pass
