#!/usr/bin/env python
#-*- coding: utf-8 -*-
#

from django import forms
from RoomManage.models import Room,RoomTemporary

class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room     
        fields = ('roomsn','name','strategys','auto_warning','is_active')
        widgets = {
            'roomsn' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'strategys' : forms.SelectMultiple(attrs={'class':'form-control','size':'10','multiple':'multiple'}),
            'auto_warning' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
            'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(AddRoomForm,self).__init__(*args,**kwargs)
        self.fields['roomsn'].label=u'机房编号'
        self.fields['roomsn'].error_messages={'required':u'请输入机房编号'}
        self.fields['name'].label=u'机房名称'
        self.fields['name'].error_messages={'required':u'请输入机房名称'}
        self.fields['strategys'].label=u'机房策略'
        self.fields['strategys'].required=False
        self.fields['auto_warning'].label=u'自动报警'
        self.fields['is_active'].label=u'是否可用'

class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('roomsn','name','strategys','auto_warning','is_active')
        widgets = {
            'roomsn' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'strategys' : forms.SelectMultiple(attrs={'class':'form-control','size':'10','multiple':'multiple'}),
            'auto_warning' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
            'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(EditRoomForm,self).__init__(*args,**kwargs)
        self.fields['roomsn'].label=u'机房编号'
        self.fields['roomsn'].error_messages={'required':u'请输入机房编号'}
        self.fields['name'].label=u'机房名称'
        self.fields['name'].error_messages={'required':u'请输入机房名称'}
        self.fields['strategys'].label=u'机房策略'
        self.fields['strategys'].required=False
        self.fields['auto_warning'].label=u'自动报警'
        self.fields['is_active'].label=u'是否可用'

# class ListRoomForm(forms.ModelForm):
#     class Meta:
#         model = Room
#         fields = ('roomsn','name','is_active')
#         widgets = {
#             'roomsn' : forms.TextInput(attrs={'class':'form-control'}),
#             'name' : forms.TextInput(attrs={'class':'form-control'}),
#             'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
#         }

#     def __init__(self,*args,**kwargs):
#         super(ListRoomForm,self).__init__(*args,**kwargs)
#         self.fields['roomsn'].label=u'机房编号'
#         self.fields['roomsn'].error_messages={'required':u'请输入账号'}
#         self.fields['name'].label=u'机房名称'
#         self.fields['name'].error_messages={'required':u'请输入密码'}
#         self.fields['is_active'].label=u'是否可用'
