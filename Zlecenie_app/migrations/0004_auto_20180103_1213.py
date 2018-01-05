# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 11:13
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('Zlecenie_app', '0003_auto_20171227_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='zlecenie',
            name='dystans',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='zlecenie',
            name='ilosc_sztuk',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='zlecenie',
            name='waga',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='zlecenie',
            name='data_zlozenia',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 3, 11, 13, 58, 911291, tzinfo=utc)),
        ),
    ]
