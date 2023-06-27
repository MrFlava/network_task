from django.contrib.auth import login, logout, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

from auth_app.serializers import LoginSerializer, JWTSerializer, UserDetailsSerializer, UserSerializer
from auth_app.utils import jwt_encode
User = get_user_model()


class RegisterView(CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Registration

        This method requires the body as \n
            {
              "username": "string",
              "email": "user@example.com",
              "first_name": "string",
              "last_name": "string",
              "password": "string",
            }
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return super(RegisterView, self).create(request, *args, **kwargs)


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = Token

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token = jwt_encode(user)
        login(request, user)

        data = {
            'user': user,
            'token': token
        }
        serializer = JWTSerializer(instance=data, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.logout(request)

    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)

        return Response({"detail": "Successfully logged out."},
                        status=status.HTTP_200_OK)


class CurrentUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserDetailsSerializer(request.user)
        return Response(serializer.data)


class RefreshTokenView(JSONWebTokenAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = RefreshJSONWebTokenSerializer
