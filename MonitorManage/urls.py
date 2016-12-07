from django.conf.urls import patterns, include, url

urlpatterns = patterns('MonitorManage.views',
    url(r'^list/(?P<SN>[0-9a-zA-Z]+)/$', 'monitor.ListRoomStatus', name='listroomstatusurl'),
    url(r'^history/(?P<SN>[0-9a-zA-Z]+)/$', 'monitor.HistoryStatus', name='historystatusurl'),
    url(r'^historydata/(?P<SN>[0-9a-zA-Z]+)/$', 'monitor.HistoryData', name='historydataurl'),

    url(r'^report/$', 'monitor.ReportRoomStatus', name='reportroomstatusurl'),
    url(r'^dowarning/(?P<SN>[0-9a-zA-Z]+)/$', 'monitor.DoWarning', name='dowarningurl'),
)
