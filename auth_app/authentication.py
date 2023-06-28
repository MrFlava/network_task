from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class TokenAuthentication(BaseAuthentication):
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        jwt_auth = JSONWebTokenAuthentication()

        try:
            ret = jwt_auth.authenticate(request)
        except exceptions.AuthenticationFailed as e:
            raise e

        return ret

    def authenticate_header(self, request):
        return f'Bearer realm="{self.www_authenticate_realm}"'
