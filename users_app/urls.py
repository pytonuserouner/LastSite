from django.urls import path, include
from rest_framework import routers

from .views import (
    SignInView,
    sign_out,
    SignUpView,
    ProfileView,
    AvatarProfileView,
    PasswordProfileView, SignInViewSet
)




# router = routers.DefaultRouter()
# router.register(r"login", SignInViewSet)


urlpatterns = [
    # path("", include((router.urls))),
    # path("sign-in", include("rest_framework.urls", namespace="rest_framework")),
    # path("sign-in", sign_in, name="login"),
    # path("sign-in", SignInViewSet.as_view(), name="login"),
    path("sign-in", SignInView.as_view(), name="login"),
    path("sign-up", SignUpView.as_view(), name="register"),
    path("sign-out", sign_out, name="logout"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/password", PasswordProfileView.as_view(), name="profile-password"),
    path("profile/avatar", AvatarProfileView.as_view(), name="profile-avatar"),
]
