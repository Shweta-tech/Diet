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
# from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    #  url(r'^register/', views.ad_role_reg, name='register'),
    # Article Upload
    url(r'^list_school/', views.list_school, name='list_school'),
    url(r'^list_nutri/',views.list_nutri,name='list_nutri'),
    url(r'^list_icds/',views.list_icds,name='list_icds'),
    # Image Upload
    url(r'^image_school/', views.image_school, name='image_school'),
    url(r'^image_nutri/', views.image_nutri, name='image_nutri'),
    url(r'^image_icds/', views.image_icds, name='image_icds'),
    # Video Upload
    url(r'^video_school/', views.video_school, name='video_school'),
    url(r'^video_nutri/',views.video_nutri_garden,name='video_nutri'),
    url(r'^video_icds/',views.video_upload_icds,name='video_icds'),
    # Display Resources 
    url(r'^resources/', views.resources, name='resources'),
    url(r'^schoolresources/', views.schoolresources, name='schoolresources'),
    url(r'^poshanvatikaresources/', views.poshanvatikaresources, name='poshanvatikaresources'),
    url(r'^icdsresources/', views.icdsresources, name='icdsresources'),

    url(r'^article_school/', views.article_school, name='article_school'),
    url(r'^resources_nutrigarden/', views.resources_nutrigarden, name='resources_nutrigarden'),
    url(r'^article_icds/', views.resources_icds, name='article_icds'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)