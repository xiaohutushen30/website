# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManage', '0004_usertemporary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserTemporary',
        ),
    ]
