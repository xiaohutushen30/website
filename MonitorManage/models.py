#-*- coding: utf-8 -*-
#

from django.db import models
from UserManage.forms import User
from RoomManage.forms import Room
from VisitorManage.forms import Visitor

class RoomStatus(models.Model):
    # id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room,null=True,blank=True)
    person = models.ForeignKey(Visitor,null=True,blank=True)
    status = models.BooleanField(default=False)
    # frid_personnumber = models.IntegerField(null=True, blank=True)
    # ir_personnumber = models.IntegerField(null=True, blank=True)
    optiontime = models.DateTimeField(null=True, blank=True)
    is_warning = models.BooleanField(default=False)

class RoomStatusGroup(models.Model):
    # id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room,null=True,blank=True)
    persons = models.CharField(max_length=64, null=True)
    frid_personnumber = models.IntegerField(null=True, blank=True)
    ir_personnumber = models.IntegerField(null=True, blank=True)
    optiontime = models.DateTimeField(null=True, blank=True)
    is_warning = models.BooleanField(default=False)
