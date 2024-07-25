from django.urls import path
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView
from rest_framework.permissions import AllowAny

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("list/", UserListAPIView.as_view(), name="user_list"),
    path("retrieve/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("destroy/", UserDestroyAPIView.as_view(), name="user_destroy"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
]
