from django import forms  
from datetimepicker.widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from .models import DailyScheduleForm,BodyModel,EatTodayModel,DietModel,FeedbackModel,studentprof
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
    
    class Meta:
        model = studentprof
        fields = ('uid','birthdate','age','contact','schoolname','schoolcordinatorincharge','schooladdress','schoolcontactinformation','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','uploaded_photo',)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model  = FeedbackModel 
        fields = ['name','issues','suggestions']
        widgets = {
            'issues': Textarea(attrs={'cols': 5, 'rows': 5}),
            'suggestions': Textarea(attrs={'cols': 5, 'rows': 5}),
        }
