from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# from .forms import Form,DocumentForm,ImageForm,DailySchedule,BodyForm,EatTodayForm,DietForm,FeedbackForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from resources.models import image_up
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
from .get_lat_lon_exif_pil import ImageMetaData
from django.http import HttpResponse
# from .resources import bulkResource
# import exiftool
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)


def show(request):
    hm= HeadMentor.objects.all()
    sm= SupportMentor.objects.all()
    aw= AnganwadiWorker.objects.all()
    stu= Student.objects.all()
    sch= School.objects.all()
    sc= SchoolCoordinator.objects.all()
    te= TechnicalExpert.objects.all()
    pm= ProjectManager.objects.all()
    # print(stu[0].contact)
    context={'hm':hm,'sm':sm,'aw':aw,'stu':stu,'sch':sch,'sc':sc,'te':te,'pm':pm}
    return render(request,'select.html',context)

def bulk_register(request):
    return render(request,'bulk_register.html')

# Create your views here.



def project_manager(request):
    return render(request, 'after_pro_manager.html')
def proj_managerIR(request):
    return render(request, 'proj_coord1.html')
def proj_coordIR(request):
    return render(request, 'proj_coord1.html')
def recorder(request):
    return render(request, 'example_simple_exportwav.html')
def map(request):
    image= image_up.objects.all()
    print(image)
    lat=long=img=[]
    for i in image:
        img = i.image
        print(img)
    # img=image
    
        meta_data =  ImageMetaData(img)
        latlng =meta_data.get_lat_lng()
        print(latlng)
        lat = latlng[0]
        long=latlng[1]
        print(lat)

        exif_data = meta_data.get_exif_data()
        arr=['lat','long']
        
        print(exif_data)
    context = {'site_url':settings.MY_SITE_URL,'lat':lat,'long':long,'media_url':settings.MEDIA_URL,'img':img}
    return render(request, 'index.html',context)


def food(request):
    if request.method== "POST":
        form = FoodForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('/food_form/')
    else:
        form = FoodForm()
        context= {
            'form' :form,
            
        }
    return render(request,'Food.html',context)

def RecipePage(request):
    if request.method== "POST":
        form = RecipeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('/recipe_form/')
    else:
        form = RecipeForm()
        context= {
            'form' :form,
            
        }
    return render(request,'RecipeForm.html',context)
   
def clock(request):
    return render(request,'new.html')
