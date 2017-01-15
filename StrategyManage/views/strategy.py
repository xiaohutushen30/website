#!/usr/bin/env python
#-*- coding: utf-8 -*-
#

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

from StrategyManage.forms import AddStrategyForm, EditStrategyForm
from StrategyManage.models import Rules, Strategys

@login_required
@PermissionVerify()
def AddStrategy(request):
    if request.method == "POST":
        form = AddStrategyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('liststrategyurl'))
    else:
        form = AddStrategyForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('StrategyManage/strategy.add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListStrategy(request):
    mList = Strategys.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('StrategyManage/strategy.list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditStrategy(request,ID):
    istrategy = Strategys.objects.get(id=ID)

    if request.method == "POST":
        form = EditStrategyForm(request.POST,instance=istrategy)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('liststrategyurl'))
    else:
        form = EditStrategyForm(instance=istrategy)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('StrategyManage/strategy.edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteStrategy(request,ID):
    Strategys.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('liststrategyurl'))