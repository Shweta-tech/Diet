from django.shortcuts import render
from .forms import DocumentForm_school,ImageForm_school,DocumentForm_nutri,VideoForm_school,VideoForm_nutri,VideoForm_icds,ImageForm_nutri,DocumentForm_icds,ImageForm_icds
from .models import document_sch,image_up_sch,document_nutri,video_sch,video_nutri,video_icds,image_up_nutri,document_icds,image_up_icds
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def list_school(request):
    if request.method == 'POST':
        form = DocumentForm_school(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"File is saved.")
            return redirect('/article_school/')
    else:
        form = DocumentForm_school() # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'list_school.html',{'form': form})
def image_school(request):
    
    if request.method == 'POST':
        form = ImageForm_school(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"Image is saved.")
            return redirect('/article_school/')
    else:
        form = ImageForm_school() # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'image_school.html',{'form': form})

def video_school(request):
    if request.method == 'POST':
        form = VideoForm_school(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"File is saved.")
            return redirect('/article_school/')
    else:
        form = VideoForm_school() # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'video_school.html',{'form': form})



def article_school(request):
    document = document_sch.objects.all()
    # print(documents)
    image = image_up_sch.objects.all()
    video = video_sch.objects.all()
    return render(request,'article_school.html',{'document': document,'image':image,'video':video})

def list_nutri(request):
    if request.method == 'POST':
        form = DocumentForm_nutri(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"File is saved.")
            return redirect('/resources_nutrigarden/')
    else:
        form = DocumentForm_nutri() # A empty, unbound form

#     # Render list page with the documents and the form
    return render(request,'list_nutri.html',{'form': form})

def image_nutri(request):
   
    if request.method == 'POST':
        form = ImageForm_nutri(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"Image is saved.")
            return redirect('/resources_nutrigarden/')
    else:
        form = ImageForm_nutri() # A empty, unbound form
     
     # Load documents for the list page
     # documents = Document.objects.all()
#     # Render list page with the documents and the form
    return render(request,'image_nutri.html',{'form': form})


def video_nutri_garden(request):
    if request.method == 'POST':
        form = VideoForm_nutri(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"File is saved.")
            return redirect('/resources_nutrigarden/')
    else:
        form = VideoForm_nutri() # A empty, unbound form

#     # Render list page with the documents and the form
    return render(request,'video_nutri.html',{'form': form})


def resources_nutrigarden(request):
   document = document_nutri.objects.all()
   # print(documents)
   image = image_up_nutri.objects.all()
   video = video_nutri.objects.all()
   return render(request,'article_nutri.html',{'document': document,'image':image,'video':video})

def list_icds(request):
    if request.method == 'POST':
        form = DocumentForm_icds(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"File is saved.")
            return redirect('/article_icds/')
    else:
        form = DocumentForm_icds() # A empty, unbound form
    return render(request,'list_icds.html',{'form': form})

def video_upload_icds(request):
    if request.method == 'POST':
        form = VideoForm_icds(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"File is saved.")
            return redirect('/article_icds/')
    else:
        form = VideoForm_icds() # A empty, unbound form
    return render(request,'video_icds.html',{'form': form})    



def image_icds(request):
    
    if request.method == 'POST':
        form = ImageForm_icds(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"Image is saved.")
            return redirect('/article_icds/')
    else:
        form = ImageForm_icds() # A empty, unbound for
    return render(request,'image_icds.html',{'form': form})

def resources_icds(request):
   document = document_icds.objects.all()
   # print(documents)
   image = image_up_icds.objects.all()
   video = video_icds.objects.all()
   return render(request,'article_icds.html',{'document': document,'image':image,'video':video})
