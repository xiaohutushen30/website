#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com
import json
import socket

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from website.common.TcpClient import ChatClient
from UserManage.views.permission import PermissionVerify

from MonitorManage.forms import ListRoomStatusForm
from MonitorManage.models import RoomStatus
from UserManage.models import User,UserTemporary
from RoomManage.models import Room,RoomTemporary

@login_required
@PermissionVerify()
def ListRoomStatus(request):
    mList = RoomStatus.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('MonitorManage/monitor.list.html',kwvars,RequestContext(request))


@login_required
@PermissionVerify()
def HistoryStatus(request):
    return render_to_response('MonitorManage/monitor.history.html',RequestContext(request))

@login_required
@PermissionVerify()
def HistoryData(request):
    mList = RoomStatus.objects.all()
    datas = []
    for info in mList:
        data = []
        data.append(info.optiontime.strftime('%Y-%m-%d %H:%M'))
        data.append(info.personnumber)
        datas.append(data)
    result_data = json.dumps(datas)
    return HttpResponse(result_data)

def ReportRoomStatus(request):
    method = request.method
    exec("req_model = request." + method)
    sn = req_model.get('sn')
    person_num = req_model.get('person_num')
    person_info = req_model.get('person_info')
    status = req_model.get('status')
    date = req_model.get('date')
    user_obj = User.objects.filter(personsn=person_info)
    room_obj = Room.objects.filter(roomsn=sn)
    if user_obj and room_obj:
        if status == "1":
            optiont_status = True
        else:
            optiont_status = False
        try:
            crs = RoomStatus(
                room = room_obj,
                person = user_obj,
                status = optiont_status,
                personnumber = person_num,
                optiontime = date,
                is_warning = False,
            )
            crs.save()
            msg = "ok"
        except Exception, e:
            msg = "failed"
    if (not user_obj) or (not room_obj):
        msg = "user not add or room not add!"
        person_obj, p_created = UserTemporary.objects.get_or_create(personsn=person_info)
        compt_room_obj, c_created = RoomTemporary.objects.get_or_create(roomsn=sn)
    if user_obj:
        msg = "user not add!"
        person_obj, p_created = UserTemporary.objects.get_or_create(personsn=person_info)
    if room_obj:
        msg = "room not add!"
        compt_room_obj, c_created = RoomTemporary.objects.get_or_create(roomsn=sn)
    return HttpResponse(msg)

@login_required
@PermissionVerify()
def DoWarning(request):
    chat_client = ChatClient()
    chat_client.do_connect()
    # chat_client.do_name("jsdfjasdhfjshfshakjhfasljhaslf")
    chat_client.sock.send("464B04211FFFF7F01FFFF7E8")
    msg = None
    while not msg:
        try:
            msg = chat_client.sock.recv(1024) #新建对象
            print msg
        except socket.timeout:
            pass
    chat_client.sock.close()
    return HttpResponse("ok")