# Django
from django.conf.urls import url

# local Django
from . import views


urlpatterns = [
    url(r'^error/$', views.error, name='error'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^select-user/$', views.selectUser, name='selectUser'),
    url(r'^create-user/$', views.createUser, name='createUser'),
    url(
        r'^select-user/edit-user/(?P<username>\w+)/$',
        views.editUser,
        name='editUser',
    ),
    url(
        r'^select-user/change-password/(?P<username>\w+)/$',
        views.changePassword,
        name='changePassword',
    ),
    url(
        r'^select-user/delete-user/(?P<username>\w+)/$',
        views.deleteUser,
        name='deleteUser',
    ),
    url(
        r'^search/(?P<searchKey>.*)/$',
        views.searchResults,
        name='searchResults',
    ),
    url(r'^view-page/(?P<title>.*)/$', views.viewPage, name='viewPage'),
    url(r'^edit-page/(?P<title>.*)/$', views.editPage, name='editPage'),
    url(r'^create-page/(?P<title>.*)/$', views.createPage, name='createPage'),
]
