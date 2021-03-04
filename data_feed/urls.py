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
    url(r'^personal/', views.personal, name='personal'),
    url(r'^eat_today/', views.eattoday, name='eat_today'),
    url(r'^body/', views.body_function, name='body'),
    url(r'^dietrecall/', views.diet_recall_function, name='dietrecall'),
    url(r'^daily_schedule/', views.daily_schedule_function, name='daily_schedule'),
    url(r'^anganwadi_workers_profile/', views.AnganwadiWorkerprofile, name='anganwadi_workers_profile'),
    url(r'^mukhya_sevika_profile/', views.MukhyaSevikaprofile, name='mukhya_sevika_profile'),
    url(r'^adolescent_anemic_girl_form/', views.adolescent_anemic_girl_form, name='adolescent_anemic_girl_form'),
    url(r'^pregnant_woman_form/', views.pregnant_woman_form, name='pregnant_woman_form'),
    url(r'^sam_mam_child_details/$', views.sam_mam_child_details,name='sam_mam_child_details'),
    url(r'^sam_mam_child_parents_profile/$',views.SMChildParentsprofile, name='sam_mam_child_parents_profile'),
    url(r'^feedbackform/', views.feedbackform, name='feedbackform'),
    url(r'^nutrigarden/', views.nutrigarden, name='nutrigarden'),
    path('change_pass/<int:id>',views.chng_pass),
    path('change_pass_up/<int:id>',views.chng_pass_up),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)