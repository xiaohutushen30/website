from django.conf.urls import patterns, include, url

urlpatterns = patterns('StrategyManage.views',
    url(r'^strategy/add/$', 'strategy.AddStrategy', name='addstrategyurl'),
    url(r'^strategy/list/$', 'strategy.ListStrategy', name='liststrategyurl'),
    url(r'^strategy/edit/(?P<ID>\d+)/$', 'strategy.EditStrategy', name='editstrategyurl'),
    url(r'^strategy/delete/(?P<ID>\d+)/$', 'strategy.DeleteStrategy', name='deletestrategyurl'),
)
