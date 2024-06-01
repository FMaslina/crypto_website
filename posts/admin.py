from django.contrib import admin
from posts.models import Post, PostImage, Image


class PostImageInline(admin.TabularInline):
    model = PostImage
    autocomplete_fields = ['image']
    extra = 1


class PostImageAdmin(admin.ModelAdmin):
    ...


class ImageAdmin(admin.ModelAdmin):
    search_fields = ["id"]


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'text_ru', 'text_en', 'text_pl', 'pub_date', 'video',)
    search_fields = ('pub_date', 'text',)
    list_filter = ('pub_date',)
    inlines = [PostImageInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(PostImage, PostImageAdmin)
