#!/usr/bin/env python
#-*- coding: utf-8 -*-
#

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

from VisitorManage.forms import EditVisitorForm, AddVisitorForm
from VisitorManage.models import Visitor

@login_required
@PermissionVerify()
def AddVisitor(request):
    if request.method == "POST":
        form = AddVisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listvisitorurl'))
    else:
        form = AddVisitorForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('VisitorManage/visitor.add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListVisitor(request):
    mList = Visitor.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('VisitorManage/visitor.list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditVisitor(request,ID):
    ivisitor = Visitor.objects.get(id=ID)

    if request.method == "POST":
        form = EditVisitorForm(request.POST,instance=ivisitor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listvisitorurl'))
    else:
        form = EditVisitorForm(instance=ivisitor)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('VisitorManage/visitor.edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteVisitor(request,ID):
    Visitor.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listvisitorurl'))