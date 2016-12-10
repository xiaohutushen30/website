#-*- coding: utf-8 -*-
from RoomManage.models import Room,RoomTemporary
from VisitorManage.models import Visitor,VisitorTemporary


class CleanTemporaryTable(object):
    """docstring for CleanTemporaryTable"""
    def process_response(self, request, response):
        all_room = Room.objects.all()
        all_user = Visitor.objects.all()
        all_tep_room = RoomTemporary.objects.all()
        all_tep_user = VisitorTemporary.objects.all()
        for room in all_room:
            for t_room in all_tep_room:
                if room.roomsn == t_room.roomsn:
                    t_room.delete()
        for user in all_user:
            for t_user in all_tep_user:
                if user.personsn == t_user.personsn:
                    t_user.delete()
        return response



        