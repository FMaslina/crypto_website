from django.db import models
from .utils import get_translate, split_into_sentences


class Image(models.Model):
    image = models.FileField(upload_to='images', null=True, blank=True, verbose_name='Изображение')


class Post(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name='Заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    text_ru = models.TextField(null=True, blank=True, verbose_name='Текст (RU)')
    text_en = models.TextField(null=True, blank=True, verbose_name='Текст (EN)')
    text_pl = models.TextField(null=True, blank=True, verbose_name='Текст (PL)')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    images = models.ManyToManyField(Image, through="PostImage")
    video = models.FileField(upload_to='videos', null=True, blank=True, verbose_name='Видео')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def save(self, *args, **kwargs):
        if self.text:
            sentences = split_into_sentences(self.text)
            if not self.text_ru:
                self.text_ru = get_translate('autodetect', 'ru', self.text, sentences)
            if not self.text_en:
                self.text_en = get_translate('autodetect', 'en', self.text, sentences)
            if not self.text_pl:
                self.text_pl = get_translate('autodetect', 'pl', self.text, sentences)

        super(Post, self).save(*args, **kwargs)


class PostImage(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
