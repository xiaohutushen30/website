#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com

from django import forms
from MonitorManage.models import RoomStatus

class ListRoomStatusForm(forms.ModelForm):
    class Meta:
        model = RoomStatus     
        fields = '__all__'
