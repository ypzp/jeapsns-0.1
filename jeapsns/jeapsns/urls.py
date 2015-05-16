from django.conf.urls import patterns, include, url


from jeapsns.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^hello/$', hello),
	(r'^$',index),
	(r'^.$',index),
	(r'^index_temp/([a-z]{1,10})/(\d{1,6})$',index_temp),
	(r'^index_temp_file/(\d{1,6})$',index_temp_file),
	(r'^time/(get)/(\d{1,2})/$',current_time),
    # 	('^/$',index),
    # Examples:
    # url(r'^$', 'jeapsns.views.home', name='home'),
    # url(r'^jeapsns/', include('jeapsns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
