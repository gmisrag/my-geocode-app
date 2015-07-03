from django.conf.urls import patterns, url
from info.views import *

urlpatterns = patterns('',
	url(r'^sgl/$', sgl, name='sgl'),
	url(r'^gl/$', gl, name='gl'),
	url(r'^sga/$', sga, name='sga'),
	url(r'^ga/$', ga, name='ga'),
	url(r'^ll/$', ll, name='ll'),
	url(r'^add/$', add, name='add'),
	url(r'^mp/$', mp, name='mp'),
)