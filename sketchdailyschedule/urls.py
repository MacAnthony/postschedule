from django.conf.urls import patterns, include, url
from allauth.account.views import LoginView

from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from schedule.views import CreatePost, EditPost, calendar_view, PostViewSet
from schedule.models import Post
from rest_framework import viewsets, routers

class PostViewSet(viewsets.ModelViewSet):
    model = Post

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)


urlpatterns = patterns('',
    url(r'^accounts/login/', LoginView.as_view(template_name='registration/login.html'), name="custom_login"),
    (r'^accounts/', include('allauth.urls')),
    
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
    url(r'^$', calendar_view, name="home_calendar_index"),
    url(r'^', include(router.urls)),
    url(r'^create/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})$', CreatePost.as_view(), name='create_post'),
    url(r'^update/(?P<id>\d+)/$', EditPost.as_view(), name='edit_post'),
    url(r'^cal/$', calendar_view, name='post_calendar_index'),
    url(r'^cal/(?P<year>\d{4})/(?P<month>\d{2})/$', calendar_view, name='post_calendar'),
    url(r'^suggestion/', TemplateView.as_view(template_name="forms/suggestion.html"), name="suggestion"),
)
