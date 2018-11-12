# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'users'