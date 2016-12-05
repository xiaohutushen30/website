# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='personsn',
            field=models.CharField(max_length=64, unique=True, null=True, db_index=True),
        ),
    ]
