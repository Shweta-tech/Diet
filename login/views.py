from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import StudentForm,MukhyaSevikaForm,AnganwadiWorkerForm,SchoolForm,SchoolCoordinatorForm,MentorForm,ProjectCoordinatorForm,TechnicalExpertForm,ProjectManagerForm,Form,PregnantWomanRegistrationForm,MentorForm,PrincipalInvestigatorsForm,WebGISExpertForm,NutritionExpertForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from tablib import Dataset
from django.http import JsonResponse
import openpyxl
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.contrib.auth.models import Group
# from DemoDiet.get_lat_lon_exif_pil import ImageMetaData
from django.http import HttpResponse
# from DemoDiet.resources import bulkResource
# import exiftool
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)

def login(request):
    if request.method== "POST":
        username=request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']
        # du = user.username
        # passwordChosen = f.decrypt(b"du")
        # decryptedPasswordDB = passwordChosen.decode('utf-8')
        # print(decryptedPasswordDB)
        user = auth.authenticate(password=password,username=username)
        # selected_field = username
        # print(selected_field)
        print(user)
        if user is not None:
            # data=User.objects.get(username=selected_field);
            # print(data)
            for group in user.groups.all():
                if group.name ==  'principal_investigator':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'project_manager':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'nutrition_expert':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'webgis_expert':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'mentor':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'school_coordinator':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'parents':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'student':
                    auth.login(request,user)
                    return redirect('/after_login/')

                if group.name ==  'anganwadi_worker':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'mukhya_sevika':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'icds_beneficiaries':
                    auth.login(request,user)
                    return redirect('/after_login/')
                if group.name ==  'nutrigarden_expert':
                    auth.login(request,user)
                    return redirect('/after_login/')
                # if group.name ==  'after_login':

            
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")


def student_login(request):
    return render(request,'new.html')


def redirectd(request,username):
        print(username)
        selected_field=username
        print(selected_field)
        data=User.objects.get(username=selected_field);
        print(data.groups.all())
        role =data.groups.all()
        print(role)
        for group in data.groups.all():
                if group.name ==  'principal_investigator':
                    return redirect('/after_login/')
                if group.name ==  'project_manager':
                    return redirect('/after_login/')
                if group.name ==  'nutrition_expert':
                    return redirect('/after_login/')
                if group.name ==  'webgis_expert':
                    return redirect('/after_login/')
                if group.name ==  'mentor':
                    return redirect('/after_login/')
                if group.name ==  'school_coordinator':
                    return redirect('/after_login/')
                if group.name ==  'parents':
                    return redirect('/after_login/')
                if group.name ==  'student':
                    return redirect('/after_login/')
                if group.name ==  'anganwadi_worker':
                    return redirect('/after_login/')
                if group.name ==  'mukhya_sevika':
                    return redirect('/after_login/')
                if group.name ==  'icds_beneficiaries':
                    return redirect('/after_login/')
                if group.name ==  'nutrigarden_expert':
                    return redirect('/after_login/')



def after_login(request):
    profile_form= SchoolCoordinatorForm()
    stu_form=StudentForm()
    data= User.objects.all()
    return render(request, 'after_login copy.html',{'profile_form':profile_form, 'stu_form':stu_form,'data':data})