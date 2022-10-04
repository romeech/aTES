from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from model_utils import Choices


class User(AbstractBaseUser):
    ROLES = Choices('admin', 'accountant', 'manager', 'worker')

    email = models.EmailField(null=False, unique=True)
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=100, choices=ROLES, default=ROLES.worker)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
