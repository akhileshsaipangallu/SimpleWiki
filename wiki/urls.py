# Django
from django.conf.urls import include
from django.conf.urls import url

# local Django
from . import views


urlpatterns = [
    url(r'^error/$', views.error, name='error'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(
        r'^search-(?P<searchKey>\w+)/$',
        views.searchResults,
        name='searchResults',
    ),
    url(r'^view-page/(?P<title>.*)/$', views.viewPage, name='viewPage'),
    url(r'^edit-page/(?P<title>.*)/$', views.editPage, name='editPage'),
    url(r'^create-page/(?P<title>.*)/$', views.createPage, name='createPage'),
]
