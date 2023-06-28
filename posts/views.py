from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Like
from posts.serializers import PostSerializer, PostUpdateSerializer, LikeSerializer
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
