from django import forms  
from datetimepicker.widgets import DateTimePicker
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from registration.models import Mentor,MukhyaSevika,AnganwadiWorker,Student,School,SchoolCoordinator,ProjectManager,User,NutriGardenExpert,PrincipalInvestigators,WebGISExpert,NutritionExpert
class Form(UserCreationForm):
    email=forms.EmailField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)

        for fieldname in ['first_name','last_name','username','email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model=User
        fields=('first_name','last_name','username','email', 'password1', 'password2')
    def save(self, commit=True):
        user= super().save(commit=False)

        user.email= self.cleaned_data['email']

        if commit:
            user.save()
            print(user)
        return user 

# class bulkreg(forms.ModelForm):  
#     class Meta:  
#         model = bulk_reg  
#         fields = ['name','email','mobile','roles','from_date','to_date']  
#         widgets = {
#             'from_date':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
#             'to_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
#         }
    

class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManager
        fields = ('contact',)

class MentorForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='MT'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = Mentor
        fields = ('dob','age','contact','address','education')

class SchoolCoordinatorForm(forms.ModelForm):
    class Meta:
        model = SchoolCoordinator
        fields = ('contact','schoolname','personaladdress',)

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('contact','name','institute',)

class StudentForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='STU'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = Student
        fields = ('contact','uid','nutrileader')

class AnganwadiWorkerForm(forms.ModelForm):
    class Meta:
        model = AnganwadiWorker
        fields = ('anganwadiname','anganwadiaddress',)

class MukhyaSevikaForm(forms.ModelForm):
    class Meta:
        model = MukhyaSevika
        fields = ('anganwadinumber',)
# class bulkreg(forms.ModelForm):  
#     class Meta:  
#         model = bulk_reg  
#         fields = ['name','mobile','dob']  
#         widgets = {
#             'dob':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
#             # 'to_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
#         }
# class DocumentForm(forms.Form):
#     title=forms.CharField(max_length=150, required=False)
#     docfile = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )
# 
class PrincipalInvestigatorsForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='PI'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = PrincipalInvestigators
        fields = ['dob','age','contact','uid']
        widgets = {
                    'dob': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }
class WebGISExpertForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='WGE'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model =  WebGISExpert
        fields = ['dob','age','contact','uid']
        widgets = {
                    'dob': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }

class NutritionExpertForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='NE'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model =  NutritionExpert
        fields = ['dob','age','contact','uid']
        widgets = {
                    'dob': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }