from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from .managers import CustomAccountManager

"""
Model from UserModel
"""


class User(AbstractBaseUser, PermissionsMixin):
    """
    User object.
    """

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('user name'), max_length=180, unique=True)
    full_name = models.CharField(_('full name'), max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return self.username
