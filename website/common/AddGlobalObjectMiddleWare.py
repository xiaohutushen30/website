#-*- coding: utf-8 -*-
from RoomManage.models import Room

class AddGlobalObjectMiddleWare(object):
    """docstring for ClassName"""
    def __init__(self):
        super(AddGlobalObjectMiddleWare, self).__init__()
        self.all_room = None

    def process_request(self, request):
        import pdb;pdb.set_trace()
        return None
 
    def process_template_response(self, request, response):
        if not self.all_room:
            self.all_room = Room.objects.all()
        import pdb;pdb.set_trace()
        return response
