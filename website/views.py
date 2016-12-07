#!/usr/bin/env python
#-*- coding: utf-8 -*-
#update:2014-08-30 by liufeily@163.com

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from RoomManage.models import Room

@login_required
def Home(request):
    return render_to_response('home.html',locals(),RequestContext(request))

def About(request):
    all_room = Room.objects.all()
    return render_to_response('about.html',locals(),RequestContext(request))
