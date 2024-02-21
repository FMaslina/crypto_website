from django.db import models


class Post(models.Model):
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image = models.FileField(upload_to='images', null=True, blank=True, verbose_name='Изображение')
    video = models.FileField(upload_to='videos', null=True, blank=True, verbose_name='Видео')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
