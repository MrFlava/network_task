from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django.db.models import Count

from posts.models import Post, Like
from posts.serializers import PostSerializer, PostUpdateSerializer, LikeSerializer, LikeByDaySerializer
from posts.filters import AnalyticsFilter
from auth_app.authentication import TokenAuthentication


class PostCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = PostSerializer


class PostRetrieveView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = PostSerializer
    lookup_field = "id"


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = PostUpdateSerializer
    lookup_field = "id"


class LikeCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = LikeSerializer


class LikeDestroyView(DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    lookup_field = "post"


# TODO: Think about the filtering, because filtering doesn't work properly
class AnalyticsVIew(ListAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = LikeByDaySerializer
    filter_class = AnalyticsFilter
    filter_backends = (OrderingFilter, )
    ordering_fields = ("date_liked", )

    def get_queryset(self):
        return Like.objects.extra(
            select={
                "date_liked": "date(posts_like.date_liked)"
            }
        ).annotate(likes=Count("pk")).order_by("-date_liked")

