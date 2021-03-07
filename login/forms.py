from django import forms  
from datetimepicker.widgets import DateTimePicker
from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from registration.models import HeadMentor,SupportMentor,MukhyaSevika,AnganwadiWorker,Student,School,SchoolCoordinator,TechnicalExpert,ProjectManager,ProjectCoordinator,User,AdolescentGirlRegistration,AnemicWomanRegistration,PregnantWomanRegistration,NutriGardenExpert
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
    
class ProjectCoordinatorForm(forms.ModelForm):
    class Meta:
        model = ProjectCoordinator
        fields = ('contact',)
        
class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManager
        fields = ('contact',)
class TechnicalExpertForm(forms.ModelForm):
    class Meta:
        model = TechnicalExpert
        fields = ('contact',)
class HeadMentorForm(forms.ModelForm):
    class Meta:
        model = HeadMentor
        fields = ('contact','address','mentortype','institute','qualification')

class SupportMentorForm(forms.ModelForm):
    class Meta:
        model = SupportMentor
        fields = ('contact','mentortype','category',)

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
class AdolescentGirlRegistrationForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='ADG'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = AdolescentGirlRegistration
        fields = ('contact','uid')

class AnemicWomanRegistrationForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='ANW'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = AnemicWomanRegistration
        fields = ('contact','uid')

class PregnantWomanRegistrationForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='PREG'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = PregnantWomanRegistration
        fields = ('contact','uid')
# class SMChildRegistrationForm(forms.ModelForm):
#     uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SMC'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
#     class Meta:
#         model = SMChildRegistration
#         fields = ('contact','uid')


# class SMChildParentsDetailsForm(forms.ModelForm):
#     class Meta:
#         model = SMChildParentsDetails
#         fields =  ['cuid','mothername','fathername','mage','fage','fatheroccupation','education','monthlyincome'] 

class NutriGardenExpertForm(forms.ModelForm):
    class Meta:
        model = NutriGardenExpert
        fields = ['contact'] 

