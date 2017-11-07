from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from ..views.cbv_viewsets import SnippetViewSet

router = DefaultRouter()
router.register(r'', SnippetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
