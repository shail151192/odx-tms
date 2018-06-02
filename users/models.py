# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class AuthUser(User):
    class Meta:
        proxy=True

    # def __init__(self, data):
    #     super(self, AuthUser).__init__(data)

    @classmethod
    def create(self):
        pass
