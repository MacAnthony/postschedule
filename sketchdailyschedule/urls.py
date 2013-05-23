from django.conf.urls import patterns, include, url
from allauth.account.views import LoginView

from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from schedule.views import CreatePost, EditPost, calendar_view

urlpatterns = patterns('',
    url(r'^accounts/login/', LoginView.as_view(template_name='registration/login.html'), name="custom_login"),
    (r'^accounts/', include('allauth.urls')),
    url(r'^$', calendar_view, name="home_calendar_index"),
    # Examples:
    # url(r'^$', 'sketchdailyschedule.views.home', name='home'),
    # url(r'^sketchdailyschedule/', include('sketchdailyschedule.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})$', CreatePost.as_view(), name='create_post'),
    url(r'^update/(?P<id>\d+)/$', EditPost.as_view(), name='edit_post'),
    url(r'^cal/$', calendar_view, name='post_calendar_index'),
    url(r'^cal/(?P<year>\d{4})/(?P<month>\d{2})/$', calendar_view, name='post_calendar'),
    url(r'^suggestion/', TemplateView.as_view(template_name="forms/suggestion.html"), name="suggestion"),
)
