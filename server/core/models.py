from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.fields import NullBooleanField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import tree
from random import randint
from .managers import UserManager
from datetime import datetime    


class User(AbstractBaseUser):
    username = models.CharField(max_length=1000, default='', blank=True, null=True, unique=True)

    # system
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.pk)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser



class Client(models.Model):
    tg_id = models.PositiveIntegerField(blank=True, null=True)
    time_started = models.DateTimeField(default=datetime.now, blank=True, null=True)