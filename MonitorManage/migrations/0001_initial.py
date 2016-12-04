# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('RoomManage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('personnumber', models.IntegerField(null=True, blank=True)),
                ('optiontime', models.DateTimeField(null=True, blank=True)),
                ('is_warning', models.BooleanField(default=False)),
                ('person', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('room', models.ForeignKey(blank=True, to='RoomManage.Room', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomTemporary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personsn', models.CharField(unique=True, max_length=64, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTemporary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roomsn', models.CharField(unique=True, max_length=64, db_index=True)),
            ],
        ),
    ]
