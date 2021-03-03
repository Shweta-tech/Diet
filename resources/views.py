from django.shortcuts import render
from .forms import DocumentForm,ImageForm
from .models import Document,image_up
from django.contrib import messages
from django.shortcuts import redirect
# from .get_lat_lon_exif_pil import ImageMetaData

# Create your views here.
def article(request):
    documents = Document.objects.all()
    # print(documents)
    image=image_up.objects.all()
    return render(request,'article.html',{'documents': documents,'image':image})

def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"File is saved.")
            return redirect('/article/')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'list.html',{'form': form})
    
def image(request):
    
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # messages.info(request,"Image is saved.")
            return redirect('/image/')
    else:
        form = ImageForm() # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,'image.html',{'form': form})