#-*- coding: utf-8 -*-
from RoomManage.models import Room

def GlobalContent(request):  # 只有一个参数（HttpRequeset 对象）
    all_room = Room.objects.all()
    context = {'rooms': all_room}
    return context