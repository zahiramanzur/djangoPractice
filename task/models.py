# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Priority(models.Model):
    priority = models.CharField(max_length=200)

    def __str__(self):
        return self.priority


class Task(models.Model):
    title_task = models.CharField(max_length=200)
    description_task = models.TextField()
    start_task = models.DateTimeField(blank=True, null=True)
    end_task = models.DateTimeField(blank=True, null=True)
    priority = models.ForeignKey(Priority)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


