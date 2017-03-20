"""SimpleWiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.contrib.auth import views as authViews
from django.conf.urls import include
from django.conf.urls import url

# local Django
from SimpleWiki import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homePage, name='homePage'),
    url(
        r'^accounts/login/$', authViews.login,
        {
            'template_name': 'wiki/loginForm.html',
        },
        name='login',
    ),
    url(r'^wiki/', include('wiki.urls')),
]
