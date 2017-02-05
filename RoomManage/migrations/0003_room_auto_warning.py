# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RoomManage', '0002_room_strategys'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='auto_warning',
            field=models.BooleanField(default=False),
        ),
    ]
