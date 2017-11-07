from django.conf.urls import url, include

from . import cbv, fbv, cbv_mixins, cbv_generics, cbv_viewsets_router

urlpatterns = [
    url(r'^fbv/', include(fbv, namespace='fbv')),
    url(r'^cbv/', include(cbv, namespace='cbv')),
    url(r'^cbv-mixins/', include(cbv_mixins, namespace='cbv_mixins')),
    url(r'^cbv-generics/', include(cbv_generics, namespace='cbv_generics')),
    url(r'^cbv-viewsets-router/', include(cbv_viewsets_router, namespace='cbv_viewsets_router')),
]
