#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
import json
import socket
import binascii

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from website.common.TcpClient import ChatClient
from UserManage.views.permission import PermissionVerify

from MonitorManage.forms import ListRoomStatusForm
from MonitorManage.models import RoomStatus, RoomStatusGroup
from VisitorManage.models import Visitor,VisitorTemporary
from RoomManage.models import Room,RoomTemporary

@login_required
@PermissionVerify()
def ListRoomStatus(request, SN):
    print SN
    room = Room.objects.get(roomsn=SN)
    mList = RoomStatus.objects.filter(room_id = room.id)

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
        'SN':SN,
    }

    return render_to_response('MonitorManage/monitor.list.html',kwvars,RequestContext(request))


@login_required
@PermissionVerify()
def HistoryStatus(request, SN):
    kwvars = {
        'request':request,
        'SN':SN,
    }
    return render_to_response('MonitorManage/monitor.history.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def HistoryData(request, SN):
    room = Room.objects.get(roomsn=SN)
    mList = RoomStatusGroup.objects.filter(room_id = room.id)
    datas_frid = []
    datas_ir = []
    datas2 = []
    reult_datas = []
    for info in mList:
        data1 = []
        data1.append(info.optiontime.strftime('%Y-%m-%d %H:%M:%S'))
        data1.append(info.frid_personnumber)
        datas_frid.append(data1)
        data2 = []
        data2.append(info.optiontime.strftime('%Y-%m-%d %H:%M:%S'))
        data2.append(info.ir_personnumber)
        datas_ir.append(data2)
    # frid_data = json.dumps(datas_frid)
    # ir_data = json.dumps(datas_ir)
    reult_datas.append(datas_frid)
    reult_datas.append(datas_ir)
    reult_datas_json = json.dumps(reult_datas)
    return HttpResponse(reult_datas_json)

def ReportRoomStatus(request):
    method = request.method
    exec("req_model = request." + method)
    sn = req_model.get('sn')
    person_num = req_model.get('person_num')
    person_info = req_model.get('person_info')
    persons_real_num = req_model.get('persons_real_num')
    date = req_model.get('date')
    is_add = True
    person_list = json.loads(person_info)
    for person in person_list:
        user_obj = Visitor.objects.filter(personsn=person["info"])
        if not user_obj:
            is_add = False
            print "Visitor %s not add"%person
    room_obj = Room.objects.filter(roomsn=sn)
    if is_add and room_obj:
        try:
            persons = []
            for person in person_list:
                user_obj = Visitor.objects.filter(personsn=person["info"])
                crs = RoomStatus(
                    room = room_obj[0],
                    person = user_obj[0],
                    status = person["status"],
                    # personnumber = 1,
                    optiontime = date,
                    is_warning = False,
                )
                crs.save()
                persons.append(str(user_obj[0].id))
                print crs.id
            rsg = RoomStatusGroup(
                room = room_obj[0],
                persons = "[" + ",".join(persons) + "]",
                frid_personnumber = persons_real_num,
                ir_personnumber = person_num,
                optiontime = date,
                is_warning = False,
            )
            rsg.save()
            msg = "ok"
        except Exception, e:
            msg = "failed"
            print "failed"
    if not is_add:
        msg = "user not add!"
        for person in person_list:
            person_obj, p_created = VisitorTemporary.objects.get_or_create(personsn=person["info"])
    if not room_obj:
        msg = "room not add!"
        compt_room_obj, c_created = RoomTemporary.objects.get_or_create(roomsn=sn)
    return HttpResponse(msg)

@login_required
@PermissionVerify()
def DoWarning(request, SN):
    chat_client = ChatClient()
    chat_client.do_connect(timeout=5)
    protocol = "464B04XX" + SN
    protocol_len = len(protocol)
    protocol = protocol.replace("XX",process_hex(protocol_len/2))
    protocol = binascii.a2b_hex(protocol)
    chat_client.sock.send(protocol)
    try:
        msg = chat_client.sock.recv(1024) #新建对象
    except socket.timeout:
        msg = "timeout"
    chat_client.sock.close()
    # return HttpResponse(msg)
    status_dict = {"success":u"手动报警成功","failure":u"手动报警失败","unknown":u"未知错误","timeout":"接收消息超时"}
    content = status_dict[msg]
    return render_to_response('modal.large.html',{"title":u"提示","content":content},RequestContext(request))

def process_hex(num):
    hex_num = hex(num)[2:].upper()
    if len(hex_num) == 1:
        hex_num = "0"+hex_num
    return hex_num