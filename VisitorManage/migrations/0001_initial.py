# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('username', models.CharField(unique=True, max_length=40, db_index=True)),
                ('personsn', models.CharField(max_length=64, unique=True, null=True, db_index=True)),
                ('id_card', models.CharField(max_length=64, unique=True, null=True, db_index=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('sex', models.CharField(max_length=2, null=True)),
                ('is_bind', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorTemporary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personsn', models.CharField(unique=True, max_length=64, db_index=True)),
            ],
        ),
    ]
