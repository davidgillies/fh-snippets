from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from tags.models import Tag

class TagViewSet(viewsets.ModelViewSet):
    model = Tag

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)

urlpatterns = patterns('', 
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

