# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    assign_to = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "<%s %s %s>"%(self.id, self.title, self.type)
