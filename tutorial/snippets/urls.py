from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.snippet_list, name='snippet_list'),
]
