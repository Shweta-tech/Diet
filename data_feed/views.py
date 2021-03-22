from django.shortcuts import render
from .forms import DailySchedule,BodyForm,EatTodayForm,DietForm,FeedbackForm,studentprofForm,mentorprofForm,scprofForm,ngprofForm,msprofForm,awprofForm,anemicadolescentgirlprofForm,anemiclactatingmotherprofForm,pregnantwomanprofForm,smparentsprofForm
from .models import DailyScheduleForm,BodyModel,EatTodayModel,DietModel,FeedbackModel,PersonalInformationForms,mentorprof,studentprof,ngprof,scprof,msprof,awprof,anemicadolescentgirlprof,anemiclactatingmotherprof,pregnantwomanprof,smparentsprof
from registration.models import User,Student
from django.contrib.auth.models import Group, User
from registration.forms import Form,StudentForm
from django.shortcuts import redirect
from .encryption_util import encrypt, decrypt
from django.contrib import messages

# Create your views here.
def chng_pass(request, id):  
    data = User.objects.get(id=id)
    data.first_name=decrypt(data.first_name)
    data.last_name=decrypt(data.last_name)
    data.email=decrypt(data.email)
    data.student.contact=decrypt(data.student.contact)
    return render(request,'pass_change.html', {'data':data}) 

def add_info(request,id):  
    
    data=User.objects.get(id=id)
    
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
            if request.method == 'POST':
                form = mentorprofForm(request.POST,request.FILES)
                print(form)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=mentorprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})
        if group.name ==  'school_coordinator':
            if request.method == 'POST':
                form = scprofForm(request.POST,request.FILES)
                print(form)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=scprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})
        if group.name ==  'parents':
            return redirect('/after_login/')
        if group.name ==  'student':
            # print(data.student.uid)
            if request.method == 'POST':
                form = studentprofForm(request.POST,request.FILES)
                print(form)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=studentprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})
        if group.name ==  'anganwadi_worker':
            if request.method == 'POST':
                form = awprofForm(request.POST,request.FILES)
                print(form)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=awprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})
        if group.name ==  'mukhya_sevika':
            if request.method == 'POST':
                form = msprofForm(request.POST,request.FILES)
                print(form)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=msprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})
        if group.name ==  'icds_beneficiaries':
            return redirect('/after_login/')
        if group.name ==  'nutrigarden_expert':
            if request.method == 'POST':
                form = ngprofForm(request.POST,request.FILES)
                print(form)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=ngprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})

        if group.name ==  'adolescent_girl':
            if request.method == 'POST':
                form = anemicadolescentgirlprofForm(request.POST,request.FILES)
                print(form)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=  anemicadolescentgirlprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})
        if group.name ==  'anemic_lactating_mother':
            if request.method == 'POST':
                form = anemiclactatingmotherprofForm(request.POST,request.FILES)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=  anemiclactatingmotherprofFrom()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})                
        if group.name ==  'anemic_pregnant_woman':
            if request.method == 'POST':
                form = pregnantwomanprofForm(request.POST,request.FILES)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=  pregnantwomanprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})                
        if group.name ==  'sam_mam_parents':
            if request.method == 'POST':
                form = smparentsprofForm(request.POST,request.FILES)
                if form.is_valid():
                    user= User.objects.get(id=id)
                    profile= form.save(commit=False)
                    profile.user=user
                    profile.save() 
                    messages.info(request,"File is saved.")
                    return redirect('/after_login/')
                else:
                    print("fail")
                    return redirect('/')

            
                # print(profile_form)
            else:
                profile_form=  smparentsprofForm()
                return render(request,'user_profile.html', {'data':data,'profile_form':profile_form})                



def consent(request):
    return render(request,'concentform.html')

def student_data(request):
    user=User.objects.filter(groups__name='student')
    # user.groups.
    
    # stu= Student.objects.all()
    
    # hulk=Group.objects.get(name='student')
    # print(hulk)
    for i in user:
        # stu= Student.objects.get(user_id=i.id)

        # print(stu.c/ontact)
        print(i.id)
        i.first_name= decrypt(i.first_name)
        i.last_name=decrypt(i.last_name)
        i.username=i.username
        i.email=decrypt(i.email)
        # i.student.contact=decrypt(i.student.contact)

    # for st in stu:
    #     # print(st.contact)
    #     st.contact=decrypt(st.contact)
    context={'user':user}
    return render(request,'show_data_student.html',context)
def chng_pass_up(request, id):
    data = User.objects.get(id=id)
    
    print(data) 
    form = Form(request.POST, instance= data) 
    # profile_form= UserProfile(request.POST, instance= form) 
    print(form)
    if form.is_valid() :
        # if User.objects.get(username=data):
        # 
        print(form.cleaned_data['password1']) 
        print("success") 
        user=form.save()
        print(user)
        # profile= profile_form.save(commit=False)
        # profile.user=user
            # profile.save(
            # )
        # if role=='admin' and 'custodian':
        #     stuff_in_string = "Hello {} Your username is {} and Password is {}.Thanks!!".format(data.username,data.username,form.cleaned_data['password1'])
        #     print(stuff_in_string)
        #             # email=i.email }}
        #     send_mail('IGMC', stuff_in_string, 'igmchospitalnagpur@gmail.com',
        #         [data.email], fail_silently=False)
        return redirect("/logout/")  
    else:
        print("fail")
    return render(request, 'pass_change.html', {'data': data}) 
def body_function(request):
    if request.method == 'POST':
        weight = request.POST.get("weight")
        weightunit= request.POST.get("weightunit")
        height= request.POST.get("height")
        heightunit= request.POST.get("heightunit")
        bmi= request.POST.get("bmi")
        waist= request.POST.get("waist")
        waistunit= request.POST.get("waistunit")
        hip= request.POST.get("hip")
        hipunit= request.POST.get("hipunit")
        whratio= request.POST.get("whratio")
        sub=BodyModel(weight=weight,weightunit=weightunit,height=height,heightunit=heightunit,bmi=bmi,waist=waist,waistunit=waistunit,hip=hip,hipunit=hipunit,whratio=whratio)
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return render(request,'eattoday.html')  

    else:
        form = BodyForm()
    return render(request,'body.html')



def feedbackform(request):
    if request.method == 'POST':
        print("after post")
        form = FeedbackForm(request.POST)
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'base.html')  

    else:
        form = FeedbackForm()
    return render(request,'feedback_form.html')

def personal(request):
    user = request.user
    id = user.id
    print(id)
    if request.is_ajax():
        print("ajax reqquest")
        selected_field = request.GET['id']
        print(selected_field)
        docinfo = list(User.objects.filter(user_id=id).values()); 
        print(docinfo)
        jsondata =docinfo[0]
        return JsonResponse(jsondata)
    if request.method== "POST":
        uniqueid = request.POST.get("uniqueid")
        name= request.POST.get("name")
        dob= request.POST.get("dob")
        age= request.POST.get("age")
        age_in_months= request.POST.get("age_in_months")
        age_in_days= request.POST.get("age_in_days")
        fname= request.POST.get("fname")
        mname= request.POST.get("mname")
        contact= request.POST.get("contact")
        email= request.POST.get("email")
        address= request.POST.get("address")
        pp= request.POST.get("pp")
        
        sub=PersonalInformationForms(uniqueid=uniqueid,name=name,dob=dob,year=age,month=age_in_months,days=age_in_days,fathername=fname,mothername=mname,contactnumber=contact,email=email,address=address,profileimage=pp)
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return render(request,'daily_schedule.html')

    else:
        return render(request,'personal.html')


def dietRecallApp(request):
    if request.method== "POST":
        form = DietRecallAppForm(request.POST)
        image_upload=ImageForm(request.POST,request.FILES)
        print(form)
        print(image_upload)
        if form.is_valid() and image_upload.is_valid():
            diet=form.save()
            print(diet)
            
            img= image_upload.save(commit=False)
            img.diet=diet
            img.save() 
        return redirect('/diet_recall_form/')
    else:
        form = DietRecallAppForm()
        image_upload= ImageForm()
        context= {
            'form' :form,
            'image_upload':image_upload
            
        }
    return render(request,'dietrecall.html',context)
def daily_schedule_function(request):
    if request.method == 'POST':
        sleepfrom = request.POST.get("sleepfrom")
        sleepto= request.POST.get("sleepto")
        eatfrom= request.POST.get("eatfrom")
        eatto= request.POST.get("eatto")
        studyfrom= request.POST.get("studyfrom")
        studyto= request.POST.get("studyto")
        playfrom= request.POST.get("playfrom")
        playto= request.POST.get("playto")
        housework= request.POST.get("housework")
        activities= request.POST.get("activities")
        
        
        sub=DailyScheduleForm(sleepfrom=sleepfrom,sleepto=sleepto,eatfrom=eatfrom,eatto=eatto,studyfrom=studyfrom,studyto=studyto,playfrom=playfrom,playto=playto,housework=housework,activities=activities)
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return render(request,'body.html')  

    else:
        form = DailySchedule()
    return render(request,'daily_schedule.html',{'form':form})

def eattoday(request):
    if request.method == 'POST':
        foodhabbits = request.POST.get("foodhabbits")
        foodallergies= request.POST.get("foodallergies")
        # eatfrom= request.POST.get("eatfrom")
        # eatto= request.POST.get("eatto")
        # studyfrom= request.POST.get("studyfrom")
        # studyto= request.POST.get("studyto")
        # playfrom= request.POST.get("playfrom")
        # playto= request.POST.get("playto")
        # housework= request.POST.get("housework")
        # activities= request.POST.get("activities")
        
        
        sub=EatTodayModel(foodhabbits=foodhabbits,foodallergies=foodallergies)
        sub.save()
        print('submitted')
        return render(request,'dietrecall.html')  

    else:
        form = EatTodayForm()
    return render(request,'eattoday.html')


def diet_recall_function(request):
    if request.method == 'POST':
        mealtype = request.POST.get("mealtype")
        timefrom= request.POST.get("timefrom")
        timeto= request.POST.get("timeto")
        recipe=request.POST.get("rec")
        rotiquantity= request.POST.get("rotiquantity")
        rotiunit= request.POST.get("rotiunit")
        ricequantity= request.POST.get("ricequantity")
        riceunit= request.POST.get("riceunit")
        pohaquantity= request.POST.get("pohaquantity")
        pohaunit= request.POST.get("pohaunit")
        upmaquantity= request.POST.get("upmaquantity")
        upmaunit = request.POST.get("upmaunit")
        teaquantity= request.POST.get("teaquantity")
        teaunit= request.POST.get("teaunit")
        coffeequantity= request.POST.get("coffeequantity")
        coffeeunit= request.POST.get("coffeeunit")
        milkquantity= request.POST.get("milkquantity")
        milkunit= request.POST.get("milkunit")
        vadaquantity= request.POST.get("vadaquantity")
        biscuitquantity= request.POST.get("biscuitquantity")
        dalquantity= request.POST.get("dalquantity")
        dalunit= request.POST.get("dalunit")
        gujratidalquantity= request.POST.get("gujratidalquantity")
        gujratidalunit= request.POST.get("gujratidalunit")
        toordalquantity= request.POST.get("toordalquantity")
        toordalunit= request.POST.get("toordalunit")
        moongdalquantity= request.POST.get("moongdalquantity")
        moongdalunit= request.POST.get("moongdalunit")
        palakquantity= request.POST.get("palakquantity")
        palakunit = request.POST.get("palakunit")
        
        
        sub=EatTodayModel(mealtype=mealtype)
        sub.save()
        print('submitted')
        return render(request,'eattoday.html')  

    else:
        form = DietForm()
    return render(request,'dietrecall.html',{'form':form})



def nutrigarden(request):
    return render(request,'nutrigarden.html')  







def edit(request, id):  
    data = User.objects.get(id=id)
    # docdata  = doctor.objects.get(id=id)  
    # print(data.date)
    # for i in data:
    student=Student.objects.get(user_id=id)
    data.first_name=decrypt(data.first_name)
    data.last_name=decrypt(data.last_name)
    data.email=decrypt(data.email)
    data.student.contact=decrypt(data.student.contact)
    return render(request,'edit.html', {'data':data,'student':student}) 

def update(request, id):
    # print(id)
    # user=User.objects.get(id=id)
    data = Student.objects.get(user_id=id) 
    # print(user)
    # user.first_name=request.POST.get('first_name')
    # print(user.first_name)
    # user.last_name=request.POST.get('last_name')
    # user.email=request.POST.get('email')
    x=request.POST.get('contact')
    print(x)
    # user.first_name=request.POST.get('first_name')
    # data.first_name=decrypt(data.first_name)
    # user.save()
    # profile=Form(request.POST,instance = user)
    
    # print(profile)
    form = StudentForm(request.POST, instance = data)  
    # print(form.contact)
    if form.is_valid(): 
        new=form.cleaned_data["contact"]
        # print(new)
        contact=decrypt(new)
        # print(contact)
        form.cleaned_data["contact"]=new
        # # my_group = Group.objects.get(name='s') 
        # # my_group.user_set.add(user)
        # profile= form.save(commit=False)
        # profile.user=new
        form.save()
        return redirect("/student_data/")  
    else:
        print("fail")
        # data.first_name=decrypt(data.first_name)
    return render(request, 'edit.html', {'data': data}) 


def destroy(request, id):  
    data = User.objects.get(id=id)  
    stu= Student.objects.get(user_id=id)
    data.delete()
    stu.delete()
    return redirect("/student_data/")  
 
