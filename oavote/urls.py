from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^vote/', include('votefrontend.urls')),
	url(r'^result/', include('voteresults.urls')),

	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),

	url(r'^', include('votestatic.urls')),
)
