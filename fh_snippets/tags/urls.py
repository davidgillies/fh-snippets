from django.conf.urls import url, patterns, include
from rest_framework import viewsets, routers
from tags.views import TagViewSet


router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)

urlpatterns = patterns('', 
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

