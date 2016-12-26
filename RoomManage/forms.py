#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com

from django import forms
from RoomManage.models import Room,RoomTemporary

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room     
        fields = ('roomsn','name','is_active')
        widgets = {
            'roomsn' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(AddRoomForm,self).__init__(*args,**kwargs)
        self.fields['roomsn'].label=u'机房编号'
        self.fields['roomsn'].error_messages={'required':u'请输入账号'}
        self.fields['name'].label=u'机房名称'
        self.fields['name'].error_messages={'required':u'请输入密码'}
        self.fields['is_active'].label=u'是否可用'

class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('roomsn','name','is_active')
        widgets = {
            'roomsn' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(EditRoomForm,self).__init__(*args,**kwargs)
        self.fields['roomsn'].label=u'机房编号'
        self.fields['roomsn'].error_messages={'required':u'请输入账号'}
        self.fields['name'].label=u'机房名称'
        self.fields['name'].error_messages={'required':u'请输入密码'}
        self.fields['is_active'].label=u'是否可用'

class ListRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('roomsn','name','is_active')
        widgets = {
            'roomsn' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(ListRoomForm,self).__init__(*args,**kwargs)
        self.fields['roomsn'].label=u'机房编号'
        self.fields['roomsn'].error_messages={'required':u'请输入账号'}
        self.fields['name'].label=u'机房名称'
        self.fields['name'].error_messages={'required':u'请输入密码'}
        self.fields['is_active'].label=u'是否可用'
