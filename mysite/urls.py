import os
from django.conf.urls import patterns, include, url
from myapp.views import *
from django.views.static import *
site_media = os.path.join(os.path.dirname(__file__),'site_media')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	(r'^site_media/(?P<path>.*)$','django.views.static.serve', 
		{'document_root': site_media}),
	(r'^$',landing_page),
	(r'^login/$','django.contrib.auth.views.login'),
	(r'^register/$', register_page),
	(r'^vendvi/$', vend_view),
	(r'^vendsearch/$', vendor_search),
	(r'^venditems/(\w+)/$',itemlist),
	(r'^add_to_cart/$', add_to_cart),
	(r'^cart/$',get_cart),
	(r'^remove_cart/$',remove_from_cart),
	(r'^sign_up/$',sign_up),
	
)
