# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-01 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_auto_20160501_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='activation_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Activation date'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='cancellation_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Cancellation date'),
        ),
    ]
