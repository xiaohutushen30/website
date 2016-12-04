#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-09-12 by liufeily@163.com
import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

from MonitorManage.forms import ListRoomStatusForm
from MonitorManage.models import RoomStatus

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
    import pdb;pdb.set_trace()
    method = request.method
    exec("req_model = request." + method)
    sn = req_model.get('sn')
    person_num = req_model.get('person_num')
    person_info = req_model.get('person_info')
    status = req_model.get('status')
    date = req_model.get('date')
    person_obj, p_created = Personinfo.objects.get_or_create(personnumber=person_info, defaults={'name': person_info, "sex":u"男"})
    compt_room_obj, c_created = ComputerRoom.objects.get_or_create(roomsn=sn, defaults={'name': sn})
    if status == "1":
        optiont_status = True
    else:
        optiont_status = False
    try:
        crs = ComputerRoomStatus(
            computerroomid = compt_room_obj.id,
            personid = person_obj.id,
            status = optiont_status,
            optiontime = date,
        )
        crs.save()
        msg = "ok"
    except Exception, e:
        msg = "failed"
    return HttpResponse(msg)