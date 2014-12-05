from django.conf.urls import patterns, url
from forum import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^detail/(?P<id>\d+)/$', views.detail, name='detail'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^add_thread/$', views.add_thread, name='add_thread'),
	url(r'^add_comment/(?P<id>\d+)/$', views.add_comment, name='add_comment'),
	url(r'^user_detail/(?P<username>[\w|\W]+)/$', views.user_detail, name='user_detail')
	)