# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 01:18
from __future__ import unicode_literals

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Klient_app', '0003_auto_20171212_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zlecenie',
            name='data_zlozenia',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 1, 18, 20, 822181, tzinfo=utc)),
        ),
    ]