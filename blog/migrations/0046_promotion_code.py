# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_auto_20170824_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='code',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
