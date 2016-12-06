# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManage', '0003_auto_20161206_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTemporary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personsn', models.CharField(unique=True, max_length=64, db_index=True)),
            ],
        ),
    ]
