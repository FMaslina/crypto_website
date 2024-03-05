from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'pub_date', 'image', 'video']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        lang = self.context.get('lang')
        if lang == 'ru':
            data['text'] = instance.text_ru
        elif lang == 'pl':
            data['text'] = instance.text_pl
        else:
            data['text'] = instance.text_en

        request = self.context.get('request')
        if data['image'] is not None:
            data['image'] = request.build_absolute_uri(instance.image.url)

        if data['video'] is not None:
            data['video'] = request.build_absolute_uri(instance.video.url)

        return data
