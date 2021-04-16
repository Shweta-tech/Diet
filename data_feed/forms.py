from django import forms  
from datetimepicker.widgets import DateTimePicker
from bootstrap_datepicker_plus import DatePickerInput

from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from .models import DailyScheduleForm,BodyModel,EatTodayModel,DietModel,FeedbackModel,studentprof,ngprof,msprof,awprof,mentorprof,scprof,anemicadolescentgirlprof,anemiclactatingmotherprof,pregnantwomanprof,smparentsprof,GeneralInformation,SocioDemographicModel



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
    # birthdate=forms.DateField(widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class'}))
    
    class Meta:
        model = studentprof
        fields = ('uid','birthdate','age','schoolname','schoolcordinatorincharge','schooladdress','schoolcontactinformation','uploaded_photo',)
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                 }
class ngprofForm(forms.ModelForm):
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = ngprof
        fields = '__all__'
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                 }
class mentorprofForm(forms.ModelForm):
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = mentorprof
        fields = '__all__'
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                 }
class msprofForm(forms.ModelForm):
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = msprof
        fields = '__all__'
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                 }
class awprofForm(forms.ModelForm):
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = awprof
        fields = '__all__'
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                 }

class scprofForm(forms.ModelForm):
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = scprof
        fields = '__all__'
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                 }
class anemicadolescentgirlprofForm(forms.ModelForm):
    unit = (('kgs','kgs'),('lbs','lbs'))
    # birthdate=forms.DateField(widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class'}))
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
   
    class Meta:
        model = anemicadolescentgirlprof
        fields = ('uid','birthdate','age','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','profile_photo','feedback')
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                   
                  
        }

class anemiclactatingmotherprofForm(forms.ModelForm):
    # birthdate=forms.DateField(widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class'}))
   
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
   
    class Meta:
        model = anemiclactatingmotherprof
        fields = ('uid','birthdate','age','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','profile_photo','feedback')
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                  
        }
class pregnantwomanprofForm(forms.ModelForm):
    # birthdate=forms.DateField(widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class'}))
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
   
    class Meta:
        model = pregnantwomanprof
        fields = ('uid','birthdate','age','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','profile_photo','feedback')
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                  
        }


class smparentsprofForm(forms.ModelForm):
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = smparentsprof
        fields = ('uid','birthdate','age','education','occupation','annualincome','ICDSname','ICDScenteraddress','ICDScentercontact','foodhabits','profile_photo')
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
                 }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model  = FeedbackModel 
        fields = ['name','issues','suggestions']
        widgets = {
            'issues': Textarea(attrs={'cols': 5, 'rows': 5}),
            'suggestions': Textarea(attrs={'cols': 5, 'rows': 5}),
        }

class GeneralInformationForm(forms.ModelForm):
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = GeneralInformation
        fields = ['name_of_volunteer','name_of_student','gender','birthdate','residential_address','pincode','name_of_school','address_of_school','pincode_of_school','personal_contact_number','religion']
        widgets = {
                    'birthdate': forms.DateInput(format=('%Y/%m/%d'), attrs={'class':'some_class', 'placeholder':'Select a date', 'type':'date'}),
        }
class SocioDemographicForm(forms.ModelForm):
       
    class Meta:
        model = SocioDemographicModel
        fields = ['i_live_with','number_of_family_members','guardian_name','guardian_age','guardian_education','guardian_occupation','monthly_family_income','ration_card_color']
        
