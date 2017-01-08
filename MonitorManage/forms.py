#!/usr/bin/env python
#-*- coding: utf-8 -*-
#

from django import forms
from MonitorManage.models import RoomStatus

class ListRoomStatusForm(forms.ModelForm):
    class Meta:
        model = RoomStatus     
        fields = '__all__'
