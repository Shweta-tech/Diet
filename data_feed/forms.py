from django import forms  
from datetimepicker.widgets import DateTimePicker
from bootstrap_datepicker_plus import DatePickerInput

from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from .models import DailyScheduleForm,BodyModel,EatTodayModel,DietModel,FeedbackModel,studentprof,ngprof,msprof,awprof,mentorprof,scprof
class DailySchedule(forms.ModelForm):
    class Meta:
        model = DailyScheduleForm
        fields = ['sleepfrom','sleepto','eatfrom','eatto','studyfrom','studyto','playfrom','playto','housework','activities']

class BodyForm(forms.ModelForm):
    class Meta:
        model = BodyModel
        fields = ['weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio']
 
class EatTodayForm(forms.ModelForm):
    class Meta:
        model = EatTodayModel
        fields = ['foodhabbits','foodallergies']


class DietForm(forms.ModelForm):
    class Meta:
        model = DietModel
        fields = ['mealtype','timefrom','timeto','rotiquantity','rotiunit','ricequantity','riceunit','pohaquantity','pohaunit','upmaquantity','upmaunit','teaquantity','teaunit','coffeequantity','coffeeunit','milkquantity','milkunit','vadaquantity','biscuitquantity','dalquantity','dalunit','gujratidalquantity','gujratidalunit','toordalquantity','toordalunit','moongdalquantity','moongdalunit','palakquantity','palakunit']

class studentprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = studentprof
        fields = ('uid','birthdate','age','schoolname','schoolcordinatorincharge','schooladdress','schoolcontactinformation','uploaded_photo',)
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class ngprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = ngprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class mentorprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = mentorprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class msprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = msprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class awprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = awprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }

class scprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = scprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class FeedbackForm(forms.ModelForm):
    class Meta:
        model  = FeedbackModel 
        fields = ['name','issues','suggestions']
        widgets = {
            'issues': Textarea(attrs={'cols': 5, 'rows': 5}),
            'suggestions': Textarea(attrs={'cols': 5, 'rows': 5}),
        }
