# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StrategyManage', '0006_auto_20170204_1518'),
        ('RoomManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='strategys',
            field=models.ManyToManyField(to='StrategyManage.StrategyList', blank=True),
        ),
    ]
