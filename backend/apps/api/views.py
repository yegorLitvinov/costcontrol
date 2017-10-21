from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication


class CustomBasicAuth(BasicAuthentication):
    def authenticate_header(self, request):
        return f'CustomBasic realm={self.www_authenticate_realm}'


class LoginView(KnoxLoginView):
    authentication_classes = (CustomBasicAuth,)
    permission_classes = tuple()

    def post(self, request, format=None):
        return super().post(request, format)
