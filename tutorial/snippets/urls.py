from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', views.snippet_detail, name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
