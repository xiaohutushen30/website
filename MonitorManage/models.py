#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com

from django.db import models
from UserManage.forms import User
from RoomManage.forms import Room

class RoomStatus(models.Model):
    # id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room,null=True,blank=True)
    person = models.ForeignKey(User,null=True,blank=True)
    status = models.BooleanField(default=False)
    personnumber = models.IntegerField(null=True, blank=True)
    optiontime = models.DateTimeField(null=True, blank=True)
    is_warning = models.BooleanField(default=False)

