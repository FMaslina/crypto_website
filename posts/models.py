from django.db import models
from .utils import get_translate


class Post(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    text_ru = models.TextField(null=True, blank=True, verbose_name='Текст (RU)')
    text_en = models.TextField(null=True, blank=True, verbose_name='Текст (EN)')
    text_pl = models.TextField(null=True, blank=True, verbose_name='Текст (PL)')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image = models.FileField(upload_to='images', null=True, blank=True, verbose_name='Изображение')
    video = models.FileField(upload_to='videos', null=True, blank=True, verbose_name='Видео')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):
        if self.text:
            self.text_ru = get_translate('autodetect', 'ru', self.text)
            self.text_en = get_translate('autodetect', 'en', self.text)
            self.text_pl = get_translate('autodetect', 'pl', self.text)

        super(Post, self).save(*args, **kwargs)
