#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

from RoomManage.forms import ListRoomForm, EditRoomForm, AddRoomForm
from RoomManage.models import Room

@login_required
@PermissionVerify()
def AddRoom(request):
    if request.method == "POST":
        form = AddRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroomurl'))
    else:
        form = AddRoomForm()

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('RoomManage/room.add.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def ListRoom(request):
    mList = Room.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('RoomManage/room.list.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def EditRoom(request,ID):
    iRoom = Room.objects.get(id=ID)

    if request.method == "POST":
        form = EditRoomForm(request.POST,instance=iRoom)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listroomurl'))
    else:
        form = EditRoomForm(instance=iRoom)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('RoomManage/room.edit.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def DeleteRoom(request,ID):
    Room.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('listroomurl'))

def AddRoomAPI(request):
    method = request.method
    exec("req_model = request." + method)
    sn = req_model.get('sn')
    roomsn = req_model.get('roomsn')
    name = req_model.get('name')
    is_active = False
    is_add = True
    room_obj = Room.objects.filter(roomsn=roomsn)
    if not room_obj:
        room = Room(roomsn=roomsn,name=name,is_active=is_active,is_add=is_add)
        room.save()
        print "add room %s" % roomsn
    else:
        print "room %s is exists" % roomsn
    return HttpResponse("ok")