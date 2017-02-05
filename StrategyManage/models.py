#-*- coding: utf-8 -*-
#

from django.db import models

class RuleList(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True)
    class_name = models.CharField(max_length=64, null=True)
    explain = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        return '%s(%s)' %(self.name,self.explain)

class StrategyList(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True)
    rules = models.ManyToManyField(RuleList,blank=True)
    remarks = models.CharField(max_length=64, null=True)
    create_time = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name