from django.conf.urls import patterns, include, url

urlpatterns = patterns('RoomManage.views',
    url(r'^room/add/$', 'room.AddRoom', name='addroomurl'),
    url(r'^room/list/$', 'room.ListRoom', name='listroomurl'),
    url(r'^room/edit/(?P<ID>\d+)/$', 'room.EditRoom', name='editroomurl'),
    url(r'^room/delete/(?P<ID>\d+)/$', 'room.DeleteRoom', name='deleteroomurl'),
)
