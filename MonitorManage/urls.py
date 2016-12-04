from django.conf.urls import patterns, include, url

urlpatterns = patterns('MonitorManage.views',
    url(r'^list/$', 'monitor.ListRoomStatus', name='listroomstatusurl'),
    url(r'^history/$', 'monitor.HistoryStatus', name='historystatusurl'),
    url(r'^historydata/$', 'monitor.HistoryData', name='historydataurl'),

    url(r'^report/$', 'monitor.ReportRoomStatus', name='reportroomstatusurl'),
)
