# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MonitorManage', '0002_auto_20161206_0018'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RoomTemporary',
        ),
        migrations.DeleteModel(
            name='UserTemporary',
        ),
    ]
