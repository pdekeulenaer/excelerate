# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name=''),
        ),
    ]
