# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50, null=True)
    isActive = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{ self.username } { self.isActive }'


