# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, null=True)),
                ('class_name', models.CharField(max_length=64, null=True)),
                ('explain', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Strategys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, null=True)),
                ('strategys', models.CharField(max_length=64, null=True)),
                ('remarks', models.CharField(max_length=64, null=True)),
                ('create_time', models.DateTimeField(null=True, blank=True)),
                ('update_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
