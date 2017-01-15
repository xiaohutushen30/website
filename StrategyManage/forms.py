#!/usr/bin/env python
#-*- coding: utf-8 -*-
#

from django import forms
from StrategyManage.models import Rules,Strategys

class AddStrategyForm(forms.ModelForm):
    class Meta:
        model = Strategys
        fields = ('name','strategys','remarks')
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'strategys': forms.TextInput(attrs={'class':'form-control'}),
            'remarks' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(AddStrategyForm,self).__init__(*args,**kwargs)
        self.fields['name'].label = u"策略名称"
        self.fields['name'].error_messages={'required':u'请填入策略名称'}
        self.fields['strategys'].label = u'报警规则'
        self.fields['strategys'].error_messages = {'required': u'请输入规则id'}
        self.fields['remarks'].label=u'策略说明'
        self.fields['remarks'].error_messages={'required':u'策略说明'}

class EditStrategyForm(forms.ModelForm):
    class Meta:
        model = Strategys
        fields = ('name','strategys','remarks')
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'strategys': forms.TextInput(attrs={'class':'form-control'}),
            'remarks' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(EditStrategyForm,self).__init__(*args,**kwargs)
        self.fields['name'].label = u"策略名称"
        self.fields['name'].error_messages={'required':u'请填入策略名称'}
        self.fields['strategys'].label = u'报警规则'
        self.fields['strategys'].error_messages = {'required': u'请输入规则id'}
        self.fields['remarks'].label=u'策略说明'
        self.fields['remarks'].error_messages={'required':u'策略说明'}

