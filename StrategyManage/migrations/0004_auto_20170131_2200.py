# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StrategyManage', '0003_auto_20170131_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategys',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='strategys',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='strategys',
            name='update_time',
        ),
    ]
