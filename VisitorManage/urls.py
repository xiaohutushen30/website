from django.conf.urls import patterns, include, url

urlpatterns = patterns('VisitorManage.views',
    url(r'^visitor/add/$', 'visitor.AddVisitor', name='addvisitorurl'),
    url(r'^visitor/list/$', 'visitor.ListVisitor', name='listvisitorurl'),
    url(r'^visitor/edit/(?P<ID>\d+)/$', 'visitor.EditVisitor', name='editvisitorurl'),
    url(r'^visitor/delete/(?P<ID>\d+)/$', 'visitor.DeleteVisitor', name='deletevisitorurl'),
)
