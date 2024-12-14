from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'image', 'created_at', 'views_count',  'is_published', 'slug')
    list_filter = ('id',)
    search_fields = ('title', 'created_at')

