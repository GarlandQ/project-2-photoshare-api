from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profiles/default.jpg", upload_to="profiles")
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username
