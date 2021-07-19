from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title