# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StrategyManage', '0002_auto_20170115_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategys',
            name='strategys',
        ),
        migrations.AddField(
            model_name='strategys',
            name='strategys',
            field=models.ManyToManyField(to='StrategyManage.Rules', blank=True),
        ),
    ]
