from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.cbv import SnippetList, SnippetDetail

urlpatterns = [
    url(r'^$', SnippetList.as_view(), name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', SnippetDetail.as_view(), name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
