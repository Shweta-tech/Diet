from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import bulkreg,StudentForm,MukhyaSevikaForm,AnganwadiWorkerForm,SchoolForm,SchoolCoordinatorForm,SupportMentorForm,HeadMentorForm,ProjectCoordinatorForm,TechnicalExpertForm,ProjectManagerForm,Form,AdolescentGirlRegistrationForm,AnemicWomanRegistrationForm,PregnantWomanRegistrationForm,SMChildRegistrationForm,SMChildParentsDetailsForm,ConcentForm,NutriGardenExpertForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from .models import bulk_reg,HeadMentor,SupportMentor,MukhyaSevika,AnganwadiWorker,Student,School,SchoolCoordinator,TechnicalExpert,ProjectManager,ProjectCoordinator,User,AdolescentGirlRegistration,AnemicWomanRegistration,PregnantWomanRegistration,SMChildRegistration,SMChildParentsDetails,ConcentForm,NutriGardenExpert
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
from .resources import bulkResource
from django.http import HttpResponse
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
import hashlib
from .encryption_util import encrypt, decrypt
# Create your views here.
def register(request):
    if request.method== "POST":
        profile_form=SchoolForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        # contact = request.POST['contact']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                print('Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,"Email address Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                if profile_form.is_valid():

                    user.save()
                    profile= profile_form.save(commit=False)
                    profile.user=user
                    profile.save()
                    
                    messages.info(request,"User created")
                    user= authenticate(username=username, password= password1)
                    login(request,user)
                    print('user created')
                    return redirect('login')


        else:
            messages.info(request,"password does not match")

            print('password does not match.')
            return redirect('register')
        return redirect('register')

    else:
        profile_form= SchoolForm()
        return render(request, "register.html",{"profile_form":profile_form})

def nutri_expert(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=TechnicalExpertForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='nutrition_expert') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= TechnicalExpertForm()
    return render(request, "nutri_expert_register.html",{"profile_form":profile_form,"form":form})
def proj_manager(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=ProjectManagerForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='project_manager') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= ProjectManagerForm()
    return render(request, "proj_manager_register.html",{"profile_form":profile_form,"form":form})

def support_mentor(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=SupportMentorForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='mentor') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= SupportMentorForm()
    return render(request, "support_mentor_register.html",{"profile_form":profile_form,"form":form})




def school(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=SchoolForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='school') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form()
        profile_form= SchoolForm()
    return render(request, "school_register.html",{"profile_form":profile_form,"form":form})

def school_coordinator_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=SchoolCoordinatorForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='school_coordinator') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form()
        profile_form= SchoolCoordinatorForm()
    return render(request, "school_coordinator_register.html",{"profile_form":profile_form,"form":form})
def student(request):
               
   

    if request.method== "POST":
        form= Form(request.POST)
        # print(form)
        profile_form=StudentForm(request.POST)
        
        # print('not valid')
        if form.is_valid() and profile_form.is_valid():
            instance = form.save(commit=False)
            profile=profile_form.save(commit=False)
            instance.first_name=f.encrypt(b"form.cleaned_data['first_name']")
            instance.last_name=f.encrypt(b"form.cleaned_data['last_name']")
            instance.email=f.encrypt(b"form.cleaned_data['email']")
            instance.username=f.encrypt(b"form.cleaned_data['username']")
            profile.contact=f.encrypt(b"form.cleaned_data['contact']")
            instance.save()
            print(instance.first_name)
            
            profile.user=instance
            print("working")
            profile.save() 
            my_group = Group.objects.get(name='student') 
            my_group.user_set.add(instance)
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
    
            print('user created')
            return redirect('/personal')
    else:
        form= Form()
        profile_form= StudentForm()
    return render(request, "student_register.html",{"profile_form":profile_form,"form":form})

def mukhya_sevika_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=MukhyaSevikaForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='mukhya_sevika') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= MukhyaSevikaForm()
    return render(request, "mukhya_Sevika_register.html",{"profile_form":profile_form,"form":form})

def anganwadi_workers_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=AnganwadiWorkerForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='anganwadi_worker') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form= AnganwadiWorkerForm()
    return render(request, "anganwadi_workers_register.html",{"profile_form":profile_form,"form":form})

def adolescent_girl_register(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=AdolescentGirlRegistrationForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='AdolescentGirl') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/adolescent_girls/')
    else:
        form= Form(request.POST)
        profile_form= AdolescentGirlRegistrationForm()
    return render(request,"adolescent_girl_register.html",{"profile_form":profile_form,"form":form})


def anemic_woman_registration(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=AnemicWomanRegistrationForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='AnemicWoman') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/anemic_woman/')
    else:
        form= Form(request.POST)
        profile_form= AnemicWomanRegistrationForm()
    return render(request,"anemic_woman_registration.html",{"profile_form":profile_form,"form":form})

def pregnant_woman_registration(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=PregnantWomanRegistrationForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='PregnantWoman') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/pregnant_woman/')
    else:
        form= Form(request.POST)
        profile_form= PregnantWomanRegistrationForm()
    return render(request,"pregnant_woman_registration.html",{"profile_form":profile_form,"form":form})

def sam_mam_child_registration(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form= SMChildRegistrationForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='SMChild') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/sam_mam_child_registration/')
    else:
        form= Form(request.POST)
        profile_form= SMChildRegistrationForm()
    return render(request,"sam_mam_child_registration.html",{"profile_form":profile_form,"form":form})

def SMChildParentsDetails(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form= SMChildParentsDetailsForm(request.POST)
        print(profile_form)
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='parents') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/sam_mam_child_parents_details_form/')
    else:
        form= Form(request.POST)
        profile_form= SMChildParentsDetailsForm()
    return render(request,"Parents.html",{"profile_form":profile_form,"form":form})

def concentform(request):
    if request.method == 'POST':
        print("after post")
        form = ConcentForm(request.POST)
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'concentform.html')  

    else:
        form = ConcentForm()
    return render(request,'concentform.html')
    
def sam_mam_child(request):
    return render(request,'sam_mam_child_form.html') 
def nutri_garden_expert(request):
    if request.method== "POST":
        form= Form(request.POST)
        print(form)
        profile_form=NutriGardenExpertForm(request.POST)
        print('not valid')
        if form.is_valid() and profile_form.is_valid():
            user=form.save()
            print(user)
            my_group = Group.objects.get(name='nutrigarden_expert') 
            my_group.user_set.add(user)
            profile= profile_form.save(commit=False)
            profile.user=user
            profile.save() 
            messages.info(request,"User created")
            firstname=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password1']
            stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(firstname,username, password)
            print(stuff_in_string)
                # email=i.email }}
            
            print('user created')
            return redirect('/after_login/')
    else:
        form= Form(request.POST)
        profile_form=  NutriGardenExpertForm()
    return render(request, "nutri_garden_expert.html",{"profile_form":profile_form,"form":form}) 

def mentor_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pm.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            id=data[0]
            print(id)
            new=encrypt(data[0])
            print(new)
            print(decrypt(new))
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=encrypt(data[0]),first_name=encrypt(data[1]),last_name=encrypt(data[2]),username=data[3],email=data[4],password=data[5]) 
                
                value.save()
                my_group = Group.objects.get(name='school_coordinator') 
                my_group.user_set.add(value)
                contact=SchoolCoordinator(contact=data[6],schoolname=data[7],personaladdress=data[8],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_pm.html")
    else:
        return render(request,"bulk_reg_pm.html")

def simple_upload_s(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pm.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all();
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='school') 
                my_group.user_set.add(value)
                contact=School(contact=data[6],name=data[7],institute=data[8],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_pm.html")
    else:
        return render(request,"bulk_reg_pm.html")
    
def simple_upload_stu(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pm.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='student') 
                my_group.user_set.add(value)
                contact=Student(contact=data[6],personaladdress=data[7],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_pm.html")
    else:
        return render(request,"bulk_reg_pm.html")

def simple_upload_aw(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pm.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='anganwadi_worker') 
                my_group.user_set.add(value)
                contact=AnganwadiWorker(contact=data[6],anganwadiname=data[7],personaladdress=data[8],anganwadiaddress=data[9],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_pm.html")
    else:
        return render(request,"bulk_reg_pm.html")

def simple_upload_ms(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pm.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='mukhya_sevika') 
                my_group.user_set.add(value)
                contact=MukhyaSevika(contact=data[6],personaladdress=data[7],anganwadinumber=data[8],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_pm.html")
    else:
        return render(request,"bulk_reg_pm.html")

def simple_upload_hm(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_pm.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='mentor') 
                my_group.user_set.add(value)
                contact=HeadMentor(contact=data[6],address=data[7],mentortype=data[8],institute=data[9],qualification=data[10],user=value)
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_pm.html")
    else:
        return render(request,"bulk_reg_pm.html")

def nutri_garden_expert_bulk(request):
    if request.method== "POST":
        bulk_resource = bulkResource()
        dataset = Dataset()
        bulk =request.FILES['myFile']
        print(bulk)
        if not bulk.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request, "bulk_reg_nge.html")

        imported_data = dataset.load(bulk.read(),format='xlsx')
        print(imported_data)
        user=User.objects.all()
        for data in imported_data:
            if User.objects.filter(username=data[3]).exists():
                messages.info(request,"Username already entered")
            
            
            else:
                value = User.objects.create_user(id=data[0],first_name=data[1],last_name=data[2],username=data[3],email=data[4],password=data[5]) 
                value.save()
                my_group = Group.objects.get(name='nutrigarden_expert') 
                my_group.user_set.add(value)
                contact=NutriGardenExpert(contact=data[6])
                contact.save()
                messages.info(request,"User created")
                print('user created')

                stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data[1],data[3], data[5])
                print(stuff_in_string)
                # email=i.email }}
                send_mail('Community Diet Diversity', stuff_in_string, 'jitendra@communitygis.net',
                    [data[4]], fail_silently=False)        
                # messages.info(request,"data entered")       
        return render(request,"bulk_reg_nge.html")
    else:
        return render(request,"bulk_reg_nge.html")