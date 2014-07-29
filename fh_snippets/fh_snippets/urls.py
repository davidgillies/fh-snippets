from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fh_snippets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.home_page', name='home'),
    url(r'^snippets/$', 'snippets.views.index', name='snippets'),
    url(r'^tags/$', 'tags.views.index', name='tags'),
    url(r'^tree/$', 'tree.views.index', name='tree'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^biogs/$', 'biogs.views.index', name='biogs'),
    url(r'^biogs/biog_view/$', 'biogs.views.biog', name='biog'),
    url(r'^biogs/new/$', 'biogs.views.new_biog', name='new_biog'),
)
