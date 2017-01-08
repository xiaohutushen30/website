# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MonitorManage', '0002_auto_20170108_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomstatusgroup',
            name='person',
        ),
        migrations.RemoveField(
            model_name='roomstatusgroup',
            name='status',
        ),
        migrations.AddField(
            model_name='roomstatusgroup',
            name='persons',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
