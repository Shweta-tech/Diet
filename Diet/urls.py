"""Diet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.conf.urls.static import static
from django.conf import settings


wagtail_urlpatterns = [
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
]
urlpatterns =[
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('',include('DemoDiet.urls')),
    path('',include('login.urls')),
    path('',include('base.urls')),
    path('',include('registration.urls')),
    path('',include('resources.urls')),
    path('',include('data_feed.urls')),
    # path('',include('base.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + wagtail_urlpatterns


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('DemoDiet.urls')),
#     path('',include('login.urls')),
#     path('',include('base.urls')),
#     path('',include('registration.urls')),
#     path('',include('resources.urls')),
#     path('',include('data_feed.urls')),
#     path('',include('CMSResources.urls')),
#     # path('',include('base.urls')),
# ] + wagtail_urlpatterns
