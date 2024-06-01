from rest_framework import serializers
from posts.models import Post, Image, PostImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class PostImageSerializer(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = PostImage
        fields = ['id', 'image']


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'pub_date', 'images', 'video']

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
        post_images = []
        if request:
            for post_image in data['images']:
                image = Image.objects.get(id=post_image['id'])
                post_images.append(request.build_absolute_uri(PostImage.objects.get(image=image).image.image))

        data['images'] = post_images

        if data['video'] is not None:
            data['video'] = request.build_absolute_uri(instance.video.url)

        return data
