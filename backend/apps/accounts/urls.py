from django.conf.urls import url
from knox.views import LogoutView

from .views import LoginView

app_name = "accounts"
urlpatterns = [
    url(r"^login/", LoginView.as_view(), name="login"),
    url(r"^logout/", LogoutView.as_view(), name="logout"),
]
