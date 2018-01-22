# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-22 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.SmallIntegerField(choices=[(0, '初级'), (1, '中级'), (2, '高级')], verbose_name='难度'),
        ),
    ]
