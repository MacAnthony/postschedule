from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from schedule.views import CreatePost, calendar

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    # Examples:
    # url(r'^$', 'sketchdailyschedule.views.home', name='home'),
    # url(r'^sketchdailyschedule/', include('sketchdailyschedule.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})$', CreatePost.as_view(), name='create_post'),
    url(r'^cal/(?P<year>\d{4})/(?P<month>\d{2})/$', calendar, name='post_calendar'),
    url(r'^cal/', calendar, name='post_calendar'),

)
