# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VisitorManage', '0002_auto_20161210_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
