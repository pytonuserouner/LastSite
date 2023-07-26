import json

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework import status, permissions, viewsets, request
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile, AvatarUser
from .serializers import ProfileSerializer, AvatarSerializer, UserSerializer


User = get_user_model()

class SignInViewSet(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class SignInViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


    def sign_in(self, request):
        if request.method == 'POST':
            user_data = json.loads(request.content)
            username = user_data.get("username")
            password = user_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                redirect("frontend/index.html")
                return Response(status=status.HTTP_201_CREATED)

            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignInView(APIView):

    def post(self, request):
        user_data = json.loads(request.body)
        username = user_data.get("username")
        password = user_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignUpView(APIView):

    def post(self, request):
        user_data = json.loads(request.data)
        name = user_data.get("name")
        username = user_data.get("username")
        password = user_data.get("password")

        try:
            user = User.objects.create_user(username=username, password=password)
            profile = Profile.objects.create(user=user, first_name=name)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def sign_out(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data, template_name='frontend/profile.html')

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(self, request):
        profile = Profile.objects.get(user=request.user)

        if not profile.check_password(request.data["currentPassword"]):
            raise ValueError("reset password failed")
        else:
            profile.set_password(request.data["newPassword"])
            profile.save()
        return Response("success", status=status.HTTP_200_OK)


class AvatarProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        avatar_img = request.FILES["avatar"]
        profile = Profile.objects.get(user=request.user)
        if profile.avatar is None:
            profile.avatar = AvatarUser.objects.create(
                src="avatar_img", alt=f"avatar{profile.user.username}"
            )
            profile.save()
        else:
            profile.avatar.src = avatar_img
            profile.avatar.save()

        serializer = AvatarSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
