from django.conf.urls import patterns, include, url

urlpatterns = patterns('StrategyManage.views',
    url(r'^strategy/add/$', 'strategy.AddStrategy', name='addstratehyurl'),
    url(r'^strategy/list/$', 'strategy.ListStrategy', name='liststratehyurl'),
    url(r'^strategy/edit/(?P<ID>\d+)/$', 'strategy.EditStrategy', name='editstratehyurl'),
    url(r'^strategy/delete/(?P<ID>\d+)/$', 'strategy.DeleteStrategy', name='deletestratehyurl'),
)
