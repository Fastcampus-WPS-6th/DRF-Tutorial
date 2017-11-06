from django.conf.urls import url, include

from . import cbv, fbv

urlpatterns = [
    url(r'^fbv/', include(fbv, namespace='fbv')),
    url(r'^cbv/', include(cbv, namespace='cbv')),
]
