from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'to_pm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^admin/', include(admin.site.urls)),
)

from django_jinja import views

handler400 = views.BadRequest.as_view()
handler403 = views.PermissionDenied.as_view()
handler404 = views.PageNotFound.as_view()
handler500 = views.ServerError.as_view()