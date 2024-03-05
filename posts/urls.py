from django.urls import path
from posts.views import PostListView, PostGetView, PostListTestView

urlpatterns = [
    path('news/list', PostListView.as_view(), name='news_list'),
    path('news/get/<int:pk>', PostGetView.as_view(), name='news_get')
]
