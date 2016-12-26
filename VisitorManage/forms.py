#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com

from django import forms
from VisitorManage.models import Visitor,VisitorTemporary

class AddVisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('personsn','username','id_card','phone','sex','is_staff')
        widgets = {
            'is_staff' : forms.RadioSelect(choices=((u'True', u'内部员工'),(u'False', u'外部员工')),attrs={'class':'list-inline'}),
            'personsn': forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'id_card' : forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'sex' : forms.RadioSelect(choices=((u'男', u'男'),(u'女', u'女')),attrs={'class':'list-inline'}),
            # 'is_bind' : forms.Select(choices=((True, u'是'),(False, u'否')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(AddVisitorForm,self).__init__(*args,**kwargs)
        self.fields['is_staff'].label = u"员工类型"
        self.fields['is_staff'].error_messages={'required':u'请选择员工类型'}
        self.fields['personsn'].label = u'标 识'
        self.fields['personsn'].error_messages = {'required': u'请输入标识'}
        self.fields['username'].label=u'姓 名'
        self.fields['username'].error_messages={'required':u'请输入姓名'}
        self.fields['id_card'].label=u'身份证'
        self.fields['id_card'].error_messages={'required':u'请输入姓名'}
        self.fields['phone'].label = u'手 机'
        self.fields['phone'].error_messages = {'required': u'请输入手机', 'invalid': u'请输入有效手机'}
        self.fields['sex'].label=u'性 别'
        self.fields['sex'].error_messages={'required':u'请选择性别'}
        # self.fields['is_bind'].label=u'绑 定'

class EditVisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('personsn','username','id_card','phone','sex','is_staff')
        widgets = {
            'is_staff' : forms.RadioSelect(choices=((u'True', u'内部员工'),(u'False', u'外部员工')),attrs={'class':'list-inline'}),
            'personsn': forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'id_card' : forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'sex' : forms.RadioSelect(choices=((u'男', u'男'),(u'女', u'女')),attrs={'class':'list-inline'}),
            # 'is_bind' : forms.Select(choices=((True, u'是'),(False, u'否')),attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(EditVisitorForm,self).__init__(*args,**kwargs)
        self.fields['is_staff'].label = u"员工类型"
        self.fields['is_staff'].error_messages={'required':u'请选择员工类型'}
        self.fields['personsn'].label = u'标 识'
        self.fields['personsn'].error_messages = {'required': u'请输入标识'}
        self.fields['username'].label=u'姓 名'
        self.fields['username'].error_messages={'required':u'请输入姓名'}
        self.fields['id_card'].label=u'身份证'
        self.fields['id_card'].error_messages={'required':u'请输入姓名'}
        self.fields['phone'].label = u'手 机'
        self.fields['phone'].error_messages = {'required': u'请输入手机', 'invalid': u'请输入有效手机'}
        self.fields['sex'].label=u'性 别'
        self.fields['sex'].error_messages={'required':u'请选择性别'}
        # self.fields['is_bind'].label=u'绑 定'

