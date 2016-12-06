# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MonitorManage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtemporary',
            old_name='personsn',
            new_name='roomsn',
        ),
        migrations.RenameField(
            model_name='usertemporary',
            old_name='roomsn',
            new_name='personsn',
        ),
    ]
