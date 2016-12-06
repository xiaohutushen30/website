#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com

from django.db import models

class Room(models.Model):
    # id = models.AutoField(primary_key=True)
    roomsn = models.CharField(max_length=64, unique=True, db_index=True)
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)
    is_add = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class RoomTemporary(models.Model):
    roomsn = models.CharField(max_length=64, unique=True, db_index=True)