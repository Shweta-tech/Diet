from django import forms  
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from bootstrap_datepicker_plus import DatePickerInput
from .models import bulk_reg,Mentor,MukhyaSevika,AnganwadiWorker,Student,School,SchoolCoordinator,TechnicalExpert,ProjectManager,ProjectCoordinator,User,AnemicPregnantWoman,SMChildParentsRegister,ConcentForm,NutriGardenExpert,AnganwadiWorkerProfile,MukhyaSevikaProfile,PrincipalInvestigators,WebGISExpert,NutritionExpert,AnemicLactatingMother,AnemicAdolescentGirl,SMChild
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
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='PM'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = ProjectManager
        fields = ('dob','age','contact','uid')
        widgets = {
                    'dob': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }
class TechnicalExpertForm(forms.ModelForm):
    class Meta:
        model = TechnicalExpert
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
        fields = ('contact','nutrileader','schoolname','schoolcordinatorincharge','schooladdress','schoolcontactinformation','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','uploaded_photo','uid',)

class AnganwadiWorkerForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='ANW'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = AnganwadiWorker
        fields = ('anganwadiname','anganwadiaddress',)
        
class MukhyaSevikaForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='MUS'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = MukhyaSevika
        fields = ('dob','age','personalcontact','icdsname','icdscenteraddress','icdscentercontact','anganwadinumber','profile_image','uid')


class bulkreg(forms.ModelForm):  
    class Meta:  
        model = bulk_reg  
        fields = ['name','mobile','dob']  
        widgets = {
            'dob':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            # 'to_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
# class DocumentForm(forms.Form):
#     title=forms.CharField(max_length=150, required=False)
#     docfile = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )
class AnemicLactatingMotherForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='ALM'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = AnemicLactatingMother
        fields =  ['dob','age','personalcontact','icdsname','icdscenteraddress','icdscentercontact','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid'] 
        widgets = {
                    'dob': DatePickerInput(format='%m/%d/%Y'), 
                  
        }




class AnemicAdolescentGirlForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='AAG'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = AnemicAdolescentGirl
        fields = ['birthdate','age','personalcontact','icdsname','icdscenteraddress','icdscentercontact','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }
class AnemicPregnantWomanForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='APW'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = AnemicPregnantWoman
        fields = ['birthdate','age','personalcontact','icdsname','icdscenteraddress','icdscentercontact','occupation','education','annualincome','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }

class SMChildForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SMC'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = SMChild
        fields = ['birthdate','age','personalcontact','icdsname','icdscenteraddress','icdscentercontact','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }


class SMChildParentsRegisterForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SMP'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = SMChildParentsRegister
        fields =  ['mothername','fathername','motherbirthdate','fatherbirthdate','motherage','fatherage','personalcontact','icdsname','icdscenteraddress','icdscentercontact','occupation','education','annualincome','cuid','uid'] 
        widgets = {
                    'motherbirthdate': DatePickerInput(format='%m/%d/%Y'), 
                    'fatherbirthdate': DatePickerInput(format='%m/%d/%Y'),
        }
class ConcentForm(forms.ModelForm):
    class Meta:
        model = ConcentForm
        fields = ['concent']
class NutriGardenExpertForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='NGE'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = NutriGardenExpert
        fields = ['dob','age','contact','uid']
        widgets = {
                    'dob': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        }

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