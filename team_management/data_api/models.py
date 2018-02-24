# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models



class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=128, blank=True, default='')
    lastName = models.CharField(max_length=128, blank=True, default='')
    phone = models.CharField(max_length=64, blank=True, default='')
    emailId = models.CharField(max_length=128, blank=True, default='')
    role = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('created',)
