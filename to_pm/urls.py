from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'forum.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^avatar/', include('avatar.urls')),
    #url(r'^search/', include('haystack.urls')),
    url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^admin/', include(admin.site.urls)),
)

from django_jinja import views

handler400 = views.BadRequest.as_view()
handler403 = views.PermissionDenied.as_view()
handler404 = views.PageNotFound.as_view()
handler500 = views.ServerError.as_view()

if 'haystack' in settings.INSTALLED_APPS:
    # minimal version
    from haystack.forms import ModelSearchForm, HighlightedSearchForm
    from haystack.query import SearchQuerySet
    from haystack.views import SearchView, search_view_factory
    sqs = SearchQuerySet().all()
    urlpatterns += patterns('haystack.views',
        url(r'^search/$', search_view_factory(
            view_class=SearchView,
            form_class=ModelSearchForm,
            searchqueryset=sqs,
            template='search/search.jinja',
            load_all=False
        ), name='haystack_search'),
    )