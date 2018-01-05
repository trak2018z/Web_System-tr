# -*- coding: utf-8 -*-

# Generated by Django 1.11.7 on 2017-12-08 23:48
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('phone', models.IntegerField(default=0)),
                ('street', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=200)),
                ('post_code', models.CharField(default='', max_length=6)),
                ('company', models.CharField(blank=True, max_length=300)),
                ('company_city', models.CharField(blank=True, max_length=200)),
                ('company_street', models.CharField(blank=True, max_length=200)),
                ('company_post_code', models.CharField(blank=True, max_length=6)),
                ('company_nip', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
