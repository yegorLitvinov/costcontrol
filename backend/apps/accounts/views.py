from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


class CustomBasicAuth(BasicAuthentication):
    def authenticate_header(self, request):
        return f'CustomBasic realm={self.www_authenticate_realm}'


class LoginView(KnoxLoginView):
    authentication_classes = (CustomBasicAuth,)
    permission_classes = (AllowAny,)
    allowed_methods = ('post',)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        return super().post(request, format)
