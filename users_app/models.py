from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator

from diplastproject.settings import BASE_DIR


# from modules.system.services.utils import ImageDirectorySave


def profile_avatar_directory_path(instance: "Profile", filename: str) -> str:
    return f"uploads/avatar/{filename}"


class AvatarUser(models.Model):
    """Model of Avatar for user profile"""

    src = models.ImageField(
        blank=True,
        null=True,
        upload_to=BASE_DIR / 'uploads/avatar/',
        # upload_to=profile_avatar_directory_path,
        validators=[FileExtensionValidator(
            allowed_extensions=('png', 'jpg', 'webp', 'jpeg'))
        ],
        verbose_name="someone",
    )
    alt = models.CharField(
        blank=True, max_length=500, verbose_name="someone else"
    )


class Profile(models.Model):
    """Model of profile of user"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    fullName = models.CharField(blank=True, max_length=200, verbose_name="полное имя")
    email = models.CharField(
        blank=True, max_length=200, verbose_name="электронная почта"
    )
    phone = models.CharField(blank=True, max_length=200, verbose_name="телефон")
    balance = models.DecimalField(
        decimal_places=2, max_digits=12, verbose_name="баланс", default=0, blank=True
    )
    avatar = models.OneToOneField(
        AvatarUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="someone",
    )
