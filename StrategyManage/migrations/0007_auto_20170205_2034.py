# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StrategyManage', '0006_auto_20170204_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strategylist',
            old_name='strategys',
            new_name='rules',
        ),
    ]
