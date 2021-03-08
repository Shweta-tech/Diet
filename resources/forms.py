from django import forms  
from datetimepicker.widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from .models import  Document,image_up,video_sch,video_nutri,video_icds,document_sch,image_up_sch,document_nutri,image_up_nutri,document_icds,image_up_icds


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'Document',)
class ImageForm(forms.ModelForm):
    class Meta:
        model = image_up
        fields = ('title', 'image',)

#  School Forms
class DocumentForm_school(forms.ModelForm):
    class Meta:
        model = document_sch
        fields = ['title', 'document',]
class ImageForm_school(forms.ModelForm):
    class Meta:
        model = image_up_sch
        fields = ('title', 'image',)
class VideoForm_school(forms.ModelForm):
    class Meta:
        model = video_sch
        fields = ('title', 'video',)


# Nutri-Garden Forms
class DocumentForm_nutri(forms.ModelForm): 
    class Meta:
        model = document_nutri
        fields = ['title', 'document',]
class ImageForm_nutri(forms.ModelForm):
    class Meta:
        model = image_up_nutri
        fields = ['title', 'image',]
class VideoForm_nutri(forms.ModelForm):
    class Meta:
        model = video_nutri
        fields = ('title', 'video',)



#  ICDS Forms
class DocumentForm_icds(forms.ModelForm): 
    class Meta:
        model = document_icds
        fields = ['title', 'document',]
class ImageForm_icds(forms.ModelForm):
    class Meta:
        model = image_up_icds
        fields = ['title', 'image',]
class VideoForm_icds(forms.ModelForm):
    class Meta:
        model = video_icds
        fields = ('title', 'video',)


