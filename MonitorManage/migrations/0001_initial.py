# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RoomManage', '0002_roomtemporary'),
        ('VisitorManage', '0004_visitortemporary'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('personnumber', models.IntegerField(null=True, blank=True)),
                ('optiontime', models.DateTimeField(null=True, blank=True)),
                ('is_warning', models.BooleanField(default=False)),
                ('person', models.ForeignKey(blank=True, to='VisitorManage.Visitor', null=True)),
                ('room', models.ForeignKey(blank=True, to='RoomManage.Room', null=True)),
            ],
        ),
    ]
