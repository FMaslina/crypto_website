from rest_framework import generics
from posts.models import Post
from posts.serializers import PostSerializer


class PostGetView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
