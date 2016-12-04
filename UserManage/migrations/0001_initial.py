# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RoleList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('permission', models.ManyToManyField(to='UserManage.PermissionList', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=40, db_index=True)),
                ('personsn', models.CharField(unique=True, max_length=64, db_index=True)),
                ('email', models.EmailField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('nickname', models.CharField(max_length=64, null=True)),
                ('sex', models.CharField(max_length=2, null=True)),
                ('role', models.ForeignKey(blank=True, to='UserManage.RoleList', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
