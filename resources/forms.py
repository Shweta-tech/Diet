from django import forms  
from datetimepicker.widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from .models import Document,image_up

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'Document',)
class ImageForm(forms.ModelForm):
    class Meta:
        model = image_up
        fields = ('title', 'image',)

