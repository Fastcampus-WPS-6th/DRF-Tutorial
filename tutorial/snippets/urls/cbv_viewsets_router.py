from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from ..views.cbv_viewsets import SnippetViewSet

router = SimpleRouter()
router.register(r'', SnippetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
