# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StrategyManage', '0005_auto_20170131_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategylist',
            name='create_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='strategylist',
            name='remarks',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='strategylist',
            name='update_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
