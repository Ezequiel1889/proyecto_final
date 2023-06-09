from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InfoAvatar(models.Model):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)