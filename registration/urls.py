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
    
   
    # url(r'^tech_expert_register/', views.tech_expert, name='tech_expert_register'),
    url(r'^nutri_expert_register/', views.nutri_expert, name='nutri_expert_register'),
    # url(r'^head_mentor_register/', views.head_mentor, name='head_mentor_register'),
    url(r'^school_register/', views.school, name='school_register'),
    url(r'^student_register/', views.student, name='student_register'),
    url(r'^school_coordinator_register/', views.school_coordinator_register, name='school_coordinator_register'),
    url(r'^mukhya_sevika_register/', views.mukhya_sevika_register, name='mukhya_sevika_register'),
    url(r'^anganwadi_workers_register/', views.anganwadi_workers_register, name='anganwadi_workers_register'),
    url(r'^support_mentor_register/', views.support_mentor, name='support_mentor_register'),
    url(r'^mentor_bulk/', views.mentor_bulk, name='mentor_bulk'),
    url(r'^adolescent_girl_registration/', views.adolescent_girl_register, name='adolescent_girl_registration'),
    url(r'^pregnant_woman_registration/', views.pregnant_woman_registration, name='pregnant_woman_registration'),
    url(r'^anemic_woman_registration/', views.anemic_woman_registration, name='anemic_woman_registeration'),
    url(r'^sam_mam_child_parents_register/$',views.SMChildParentsRegister, name='sam_mam_child_parents_register'),
    url(r'^nutri_garden_expert_register/$', views.nutri_garden_expert, name='nutri_garden_expert_register'),
    url(r'^nutri_garden_expert_bulk/', views.nutri_garden_expert_bulk, name='nutri_garden_expert_bulk'),
    url(r'^concentform/$', views.concentform, name='concentform'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)