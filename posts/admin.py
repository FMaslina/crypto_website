from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'image', 'video',)
    search_fields = ('pub_date', 'text',)
    list_filter = ('pub_date',)


admin.site.register(Post, PostAdmin)
