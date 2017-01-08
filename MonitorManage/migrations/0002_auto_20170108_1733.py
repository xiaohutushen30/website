# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RoomManage', '0002_roomtemporary'),
        ('VisitorManage', '0005_visitor_id_card'),
        ('MonitorManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomStatusGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('frid_personnumber', models.IntegerField(null=True, blank=True)),
                ('ir_personnumber', models.IntegerField(null=True, blank=True)),
                ('optiontime', models.DateTimeField(null=True, blank=True)),
                ('is_warning', models.BooleanField(default=False)),
                ('person', models.ForeignKey(blank=True, to='VisitorManage.Visitor', null=True)),
                ('room', models.ForeignKey(blank=True, to='RoomManage.Room', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='roomstatus',
            name='personnumber',
        ),
    ]
