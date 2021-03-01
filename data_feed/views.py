from django.shortcuts import render
from .forms import DailySchedule,BodyForm,EatTodayForm,DietForm,FeedbackForm
from .models import DailyScheduleForm,BodyModel,EatTodayModel,DietModel,FeedbackModel
from registration.models import User
from registration.forms import Form
from django.shortcuts import redirect

# Create your views here.
def daily_schedule_function(request):
    if request.method == 'POST':
        form = DailySchedule(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
        return render(request,'eattoday.html')  

    else:
        form = DailySchedule()
    return render(request,'daily_schedule.html',{'form':form})

def eattoday(request):
    if request.method == 'POST':
        form = EatTodayForm(request.POST)
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'dietrecall.html')  

    else:
        form = EatTodayForm()
    return render(request,'eattoday.html')
def chng_pass(request, id):  
    data = User.objects.get(id=id)
    # docdata  = doctor.objects.get(id=id)  
    # print(data.userprofile.role)
    # if data.userprofile.role=='admin' and 'custodian':
    #     return render(request,'bed_dash/confirmation.html', {'data':data})
    # else:
    return render(request,'pass_change.html', {'data':data})  

def chng_pass_up(request, id):
    data = User.objects.get(id=id) 
    # role=data.userprofile.role
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
        form = BodyForm(request.POST)
        print("bodyfunction")
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'daily_schedule.html')  

    else:
        form = BodyForm()
    return render(request,'body.html')
def diet_recall_function(request):
    if request.method == 'POST':
        print("after post")
        form = DietForm(request.POST)
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'eattoday.html')  

    else:
        form = DietForm()
    return render(request,'dietrecall.html',{'form':form})

def adolescent_girls(request):
    #  if request.method == 'POST':
    #     form = EatTodayForm(request.POST)
    #     print(form)
    #     if form.is_valid():
    #             form.save()
    #             print("saved")
    #     return render(request,'dietrecall.html')  

    # else:
    #     form = EatTodayForm()
    return render(request,'Adolescent_girls_form.html')
def anemic_woman(request):
    return render(request,'Anemic_woman_form.html')
def pregnant_woman(request):
    return render(request,'Pregnant_woman_form.html')
def sam_mam_mother(request):
    return render(request,'sam_mam_mother_form.html')  

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
    return render(request,'Adolescent_girls_form.html')

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
        form = DailySchedule(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
        return render(request,'eattoday.html')  

    else:
        form = DailySchedule()
    return render(request,'daily_schedule.html',{'form':form})

def eattoday(request):
    if request.method == 'POST':
        form = EatTodayForm(request.POST)
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'dietrecall.html')  

    else:
        form = EatTodayForm()
    return render(request,'eattoday.html')

def body_function(request):
    if request.method == 'POST':
        form = BodyForm(request.POST)
        print("bodyfunction")
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'daily_schedule.html')  

    else:
        form = BodyForm()
    return render(request,'body.html')
def diet_recall_function(request):
    if request.method == 'POST':
        print("after post")
        form = DietForm(request.POST)
        print(form)
        if form.is_valid():
                form.save()
                print("saved")
        return render(request,'eattoday.html')  

    else:
        form = DietForm()
    return render(request,'dietrecall.html',{'form':form})

def adolescent_girls(request):
    #  if request.method == 'POST':
    #     form = EatTodayForm(request.POST)
    #     print(form)
    #     if form.is_valid():
    #             form.save()
    #             print("saved")
    #     return render(request,'dietrecall.html')  

    # else:
    #     form = EatTodayForm()
    return render(request,'Adolescent_girls_form.html')
def anemic_woman(request):
    return render(request,'Anemic_woman_form.html')
def pregnant_woman(request):
    return render(request,'Pregnant_woman_form.html')
def sam_mam_mother(request):
    return render(request,'sam_mam_mother_form.html')  

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
    return render(request,'Adolescent_girls_form.html')

def nutrigarden(request):
    return render(request,'nutrigarden.html')  