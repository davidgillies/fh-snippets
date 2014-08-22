# from django.conf.urls import url, patterns, include
# from rest_framework import viewsets, routers
# from tags.views import TagViewSet


# router = routers.DefaultRouter()
# router.register(r'tags', TagViewSet)

# urlpatterns = patterns('',
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include(
#           'rest_framework.urls', namespace='rest_framework')),
# )

from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from tags import views
from rest_framework import viewsets, routers

urlpatterns = patterns('',
                       url(r'^$', views.TagList.as_view(), name='tag-list'),
                       url(r'^(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),
                       # url(r'^', include(router.urls)),
                       # url(r'^api-auth/$', include(
                       # 'rest_framework.urls', namespace='rest_framework')),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
