# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]