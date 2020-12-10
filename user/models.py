
from django.contrib.auth.models import AbstractUser
from django.db import models


def user_avatars_path_generator(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user/<id>/<filename>
    return f"user/{instance.pk}/avatars/{filename}"


class User(AbstractUser):
    avatar = models.ImageField(upload_to=user_avatars_path_generator)
