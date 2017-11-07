from django.conf.urls import url, include

from . import cbv, fbv, cbv_mixins, cbv_generics

urlpatterns = [
    url(r'^fbv/', include(fbv, namespace='fbv')),
    url(r'^cbv/', include(cbv, namespace='cbv')),
    url(r'^cbv-mixins/', include(cbv_mixins, namespace='cbv_mixins')),
    url(r'^cbv-generics/', include(cbv_generics, namespace='cbv_mixins')),
]
