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
            ru_text = get_translate('autodetect', 'ru', self.text)
            en_text = get_translate('autodetect', 'en', self.text)
            pl_text = get_translate('autodetect', 'pl', self.text)

            equal_languages_error_message = "PLEASE SELECT TWO DISTINCT LANGUAGES"

            self.text_ru = ru_text if ru_text != equal_languages_error_message else self.text
            self.text_en = en_text if en_text != equal_languages_error_message else self.text
            self.text_pl = pl_text if pl_text != equal_languages_error_message else self.text

        super(Post, self).save(*args, **kwargs)
