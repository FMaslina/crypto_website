from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'text_ru', 'text_en', 'text_pl', 'pub_date', 'image', 'video',)
    search_fields = ('pub_date', 'text',)
    list_filter = ('pub_date',)


admin.site.register(Post, PostAdmin)
