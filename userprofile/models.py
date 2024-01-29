from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Userprofile(models.Model):
    # One to One account of a user
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
