#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com

from django.db import models

class Visitor(models.Model):
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=40, unique=True, db_index=True)
    personsn = models.CharField(max_length=64, unique=True, db_index=True, null=True)
    id_card = models.CharField(max_length=64, unique=True, db_index=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    sex = models.CharField(max_length=2, null=True)
    is_bind = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    def __unicode__(self):
        return self.username

class VisitorTemporary(models.Model):
    personsn = models.CharField(max_length=64, unique=True, db_index=True)