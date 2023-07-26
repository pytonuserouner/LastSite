from django.contrib import admin

from .models import AvatarUser, Profile


@admin.register(AvatarUser)
class AvatarUserAdmin(admin.ModelAdmin):
    list_display = [
        "src",
        "alt",
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "fullName",
        "email",
        "phone",
        "balance",
        "avatar",
    ]
