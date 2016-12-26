# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VisitorManage', '0004_visitortemporary'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='id_card',
            field=models.CharField(max_length=64, unique=True, null=True, db_index=True),
        ),
    ]
