# Description: This file contains the URL patterns for the account app.
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginUserView, LogoutUserView, RegisterUserView, UserDetailView

app_name = "auth"
urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("profile/", UserDetailView.as_view(), name="profile"), 
]
