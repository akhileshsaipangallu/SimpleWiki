# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_auto_20170320_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
