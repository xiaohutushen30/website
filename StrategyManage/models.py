#-*- coding: utf-8 -*-
#

from django.db import models

class Rules(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True)
    class_name = models.CharField(max_length=64, null=True)
    explain = models.CharField(max_length=64, null=True)

class Strategys(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True)
    strategys = models.CharField(max_length=64, null=True)
    remarks = models.CharField(max_length=64, null=True)
    create_time = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)