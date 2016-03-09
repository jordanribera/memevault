# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnicodeMacro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortcut', models.CharField(max_length=64, unique=True)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
