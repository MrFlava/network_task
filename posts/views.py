from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from posts.serializers import PostSerializer, PostUpdateSerializer
from auth_app.authentication import TokenAuthentication


class RestaurantCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = PostSerializer


# class RestaurantUpdateView(RestaurantMixin, UpdateAPIView):
#     permission_classes = (IsAuthenticated, )
#     authentication_classes = (TokenAuthentication,)
#     serializer_class = RestaurantUpdateSerializer
