#!/usr/bin/env python
#-*- coding: utf-8 -*-
#

from django import forms
from StrategyManage.models import RuleList,StrategyList


class StrategyForm(forms.ModelForm):
    class Meta:
        model = StrategyList
        fields = ('name','rules','remarks')
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'rules' : forms.SelectMultiple(attrs={'class':'form-control','size':'10','multiple':'multiple'}),
            'remarks' : forms.TextInput(attrs={'class':'form-control'}),
            #'permission' : forms.CheckboxSelectMultiple(choices=[(x.id,x.name) for x in PermissionList.objects.all()]),
        }

    def __init__(self,*args,**kwargs):
        super(StrategyForm,self).__init__(*args,**kwargs)
        self.fields['name'].label=u'名 称'
        self.fields['name'].error_messages={'required':u'请输入名称'}
        self.fields['rules'].label=u'策 略'
        self.fields['rules'].required=False
        self.fields['remarks'].label=u'备 注'

