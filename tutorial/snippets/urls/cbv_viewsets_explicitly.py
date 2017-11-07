from django.conf.urls import url

from ..views.cbv_viewsets import SnippetViewSet

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    url(r'^$', snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', snippet_detail, name='snippet_detail'),
]
