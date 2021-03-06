# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0010_auto_20170320_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='editPermissionLevel',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='viewPermissionLevel',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userLevel',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
