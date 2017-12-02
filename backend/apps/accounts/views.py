from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


class CustomBasicAuth(BasicAuthentication):
    def authenticate_header(self, request):
        return f'CustomBasic realm={self.www_authenticate_realm}'


class LoginView(KnoxLoginView):
    authentication_classes = (CustomBasicAuth,)
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        if request.user.is_anonymous:
            raise NotAuthenticated()
        return super().post(request, format)
