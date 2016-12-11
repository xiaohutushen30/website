#-*- coding: utf-8 -*-
from RoomManage.models import Room
import socket

def GlobalContent(request):  # 只有一个参数（HttpRequeset 对象）
    all_room = Room.objects.all()
    websocket_ip = socket.gethostbyname(socket.gethostname())
    websocket_url = websocket_ip + ":8088"
    context = {'rooms': all_room,"websocket_url":websocket_url}
    return context