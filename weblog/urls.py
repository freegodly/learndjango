from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from weblog.views import *


urlpatterns = [
    url(r'^$', home),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^home/$', home, name = 'home'),
    url(r'^details/(\d+)/$', details, name = 'details'),
]