# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StrategyManage', '0004_auto_20170131_2200'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rules',
            new_name='RuleList',
        ),
        migrations.RenameModel(
            old_name='Strategys',
            new_name='StrategyList',
        ),
    ]
