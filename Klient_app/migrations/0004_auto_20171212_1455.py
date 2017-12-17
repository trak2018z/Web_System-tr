# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 13:55
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('Klient_app', '0003_auto_20171212_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adres',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='data_zlozenia',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 13, 55, 15, 676279, tzinfo=utc)),
        ),
    ]
