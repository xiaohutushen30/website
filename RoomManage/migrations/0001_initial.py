# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roomsn', models.CharField(unique=True, max_length=64, db_index=True)),
                ('name', models.CharField(max_length=64)),
                ('is_active', models.BooleanField(default=False)),
                ('is_add', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RoomTemporary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roomsn', models.CharField(unique=True, max_length=64, db_index=True)),
            ],
        ),
    ]
