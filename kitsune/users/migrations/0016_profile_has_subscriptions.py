# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-02 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20190523_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='has_subscriptions',
            field=models.BooleanField(default=False),
        ),
    ]
