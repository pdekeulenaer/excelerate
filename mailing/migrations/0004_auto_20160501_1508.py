# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-01 22:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_auto_20160501_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
