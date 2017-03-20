# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20170320_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='editPermissionLevel',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='viewPermissionLevel',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1),
        ),
    ]
