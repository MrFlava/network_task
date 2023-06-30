from django.urls import path

from posts.views import (
    PostCreateView,
    PostRetrieveView,
    PostUpdateView,
    LikeCreateView,
    LikeDestroyView,
    AnalyticsVIew
)

app_name = "posts"

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<int:id>/info/', PostRetrieveView.as_view(), name='post-info'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post-update'),

    path('like/', LikeCreateView.as_view(), name='like-post'),
    path('<int:post>/unlike/', LikeDestroyView.as_view(), name='unlike-post'),
    path('analytics/', AnalyticsVIew.as_view(), name='likes_analytics')
]
