# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlParse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('timeshift', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'just created'), (1, 'add to queue'), (2, 'parse success'), (-1, 'parse success')], default=0, editable=False)),
                ('page_title', models.CharField(blank=True, editable=False, max_length=15, null=True)),
                ('page_charset', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('page_h1_tag', models.CharField(blank=True, editable=False, max_length=255, null=True)),
            ],
        ),
    ]
