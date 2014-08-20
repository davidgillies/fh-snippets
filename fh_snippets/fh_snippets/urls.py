from django.conf.urls import patterns, include, url
from tags.views import TagsIndex, TagsDetailView
from biogs.views import BiogView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fh_snippets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.home_page', name='home'),
    url(r'^snippets/$', 'snippets.views.index', name='snippets'),
    url(r'^tags/detail/$', TagsDetailView.as_view() ),
    url(r'^tags/$', TagsIndex.as_view()),
    url(r'^tree/upload_file/$', 'tree.views.upload_file', name='upload_file'),
    url(r'^tree/$', 'tree.views.index', name='tree'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^biogs/$', include('biogs/urls')),
    url(r'^biogs/$', BiogView.as_view(), name='biogs'),
    #url(r'^biogs/biog_view/$', 'biogs.views.biog', name='biog'),
    url(r'^biogs/new/$', 'biogs.views.new_biog', name='new_biog'),
    url(r'^biogs/(\d+)/save_notes', 'biogs.views.save_notes', name='save_notes'),
    url(r'^biogs/(\d+)/remove_snippets','biogs.views.remove_snippets', name='remove_snippets'),
    url(r'^biogs/(\d+)/remove_tags', 'biogs.views.remove_tags', name='remove_tags'),
    url(r'^biogs/(\d+)/add_tags','biogs.views.add_tags', name='add_tag'),
    url(r'^biogs/(\d+)/add_snippets', 'biogs.views.add_snippets', name='add_snippet'),
    url(r'^biogs/(\d+)/add_families', 'biogs.views.add_families', name='add_families'),
    url(r'^biogs/(\d+)/', 'biogs.views.biog', name='biog'),
)
