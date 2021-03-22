

# Create your models here.
from datetime import datetime 
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string
from django_cryptography.fields import encrypt
from uuid import UUID
from fernet_fields import EncryptedTextField



Qualification = [
            ('BSc', 'BSc'),
            ('BSW', 'BSW'),

]
Institute = [
            ('Organization', 'Organization'),
            ('College', 'College'),
            ('School','School')
]
Category = [
            ('Parent', 'Parent'),
            ('Teacher', 'Teacher'),
            ('Student', 'Student'),

]
unit = [('kgs','kgs'),('lbs','lbs')]
hunit = [('cms','cms'),('inches','inches')]
hgtunit = [ ('feet','feet'), ('inches','inches'),('cms','cms'),('inches','inches')]
nutirleader = [('Nutri-Leader','Nutri-Leader'),('School-Student','School-Student')]
foodhabit = [('Vegetarian','Vegetarian'),('Non-Vegetarian','Non-Vegetarian'),
  
]
occupation = [('Legislators,Senior Officials & Managers','Legislators,Senior Officials & Managers'),
    ('Professionals','Professionals'),
    ('Technicians and Associate Professionals','Technicians and Associate Professionals'),
    ('Clerks','Clerks'),
    ('Skilled workers and Shop & Market sales workers ','Skilled workers and Shop & Market sales workers '),
    ('Skilled Agricultural','Skilled Agricultural and Fishery workers'), 
    ('Craft and Related Trade Workers','Craft and Related Trade Workers'),
    ('Plant and Machine Operators and Assemblers','Plant and Machine Operators and Assemblers'),
    ('Elementary Occupation','Elementary Occupation'), 
    ('Security guard','Security guard'),
    ('Housekeeper or Housemaid','Housekeeper or Housemaid'),
    ('Nurse','Nurse'),
    ('Anganwadi Worker','Anganwadi Worker'),
    ('Retired','Retired'),
    ('Others','Others'),


]
education = [ ('Professionaldegree','Professionaldegree'),
    ('Graduate','Graduate (Bachelors)'),
    ('Middleschool','Middle school (5th to 10th std)'),
    ('Primaryschool','Primary school (1st to 4th std)'),
    ('Illiterate','Illiterate (No education)'),
]
annualincome =  [ ('199,862','199,862'),
    ('99,931-199,861','99,931-199,861'),
    ('74,755-99,930','74,755-99,930'),
    ('49,962-74,755','49,962-74,755'),
    ('29,973-49,961','29,973-49,961'),
    ('10,002-29,97','10,002-29,97'),
    ('10,001','10,001'),
]
pos =[('teaching-staff','Teaching Staff'),('non-teaching-staff','Non-Teaching Staff'),('principal','Principal')
]
# Create your models here.
trimester = [('1st','1st'),('2nd','2nd'),('3rd','3rd')]
child = [('SAM','SAM'),('MAM','MAM')]
class anemicadolescentgirl(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,primary_key=True,default=False)
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)   
   
class AnemicLactatingMother(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,primary_key=True,default=False)
    personalcontact = models.CharField(max_length = 200)
    childbirthdate = models.DateField(null=True, blank=True)
    ICDSname = models.CharField(max_length = 200)   
    
class AnemicPregnantWoman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,primary_key=True,default=False)
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)   
    trimester = models.CharField(choices = trimester,max_length = 10,null = True)

 


# class ProjectManager(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     uid = models.CharField(max_length=255,primary_key=True,default=False)
#     birthdate = models.DateField(null=True, blank=True)
#     age = models.CharField(max_length=255)
#     contact=models.CharField(max_length=255,blank=True)
   
#     def __str__(self):
#         return self.user.username

# class NutritionExpert(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     uid = models.CharField(max_length=255,primary_key=True,default=False)
#     birthdate = models.DateField(null=True, blank=True)
#     age = models.CharField(max_length=255)
#     contact=models.CharField(max_length=255,blank=True)

class NutriGardenExpert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,primary_key=True,default=False)
    contact=models.CharField(max_length=255,blank=True)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,primary_key=True,default=False)
    contact=models.CharField(max_length=255,blank=True)
    
   

# class School(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     contact=models.CharField(max_length=255,blank=True)
#     name = models.CharField(max_length=200,null=True)
#     institute = models.CharField(choices=Institute,default=False,max_length=20)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid =models.CharField(primary_key=True,max_length=1000)
    nutrileader = models.CharField(choices=nutirleader,default=False,max_length=20)
    contact=models.CharField(max_length=25500,blank=True)


class SMChild(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,primary_key=True,default=False)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=255)
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)
    ICDScenteraddress = models.CharField(max_length = 200)
    ICDScentercontact = models.CharField(max_length = 200)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length=255,choices=unit )
    height = models.IntegerField()
    heightunit = models.CharField(max_length = 50,choices=hgtunit)
    bmi= models.DecimalField(max_digits = 10,decimal_places = 3)
    waist = models.IntegerField(null=True)
    waistunit = models.CharField(max_length=20,choices=hunit)
    hip = models.IntegerField(null=True)
    hipunit = models.CharField(max_length=20,choices=hunit)
    whratio = models.DecimalField(max_digits = 10,null=True,decimal_places = 3)
    whratioderived = models.IntegerField(null=True)
    foodhabits =  models.CharField(max_length = 20,choices=foodhabit,null = True)
    uploaded_photo = models.FileField(upload_to='smchilddocuments/%Y/%m/%d')
  

class SMChildParentsRegister(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    uid = models.CharField(max_length=255,primary_key=True,default=False)
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)
    childis= models.CharField(max_length = 50,choices = child,null = True)
    childfirstname = models.CharField(max_length = 200,null = True)
    childlastname = models.CharField(max_length = 200,null = True)
    childbirthdate = models.DateField(null=True, blank=True)

class ConcentForm(models.Model):
    concent = models.CharField(max_length=255)


# class PrincipalInvestigators(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     uid = models.CharField(max_length=255,primary_key=True,default=False)
#     birthdate = models.DateField(null=True, blank=True)
#     age = models.CharField(max_length=255)
#     contact = models.CharField(max_length=255)
   

# class WebGISExpert(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     uid = models.CharField(max_length=255,primary_key=True,default=False)
#     birthdate = models.DateField(null=True, blank=True)
#     age = models.CharField(max_length=255)
#     contact = models.CharField(max_length=255)
   
    
class   SchoolCoordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,primary_key=True,default=False)
    contact=models.CharField(max_length=25500,blank=True)
    schoolname=  models.CharField(max_length=2000)
    schoolcontact=models.CharField(max_length=25500,blank=True)
    position=models.CharField(choices=pos,max_length=200,null=True)
    
class MukhyaSevika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,default=False)
    ICDSname=  models.CharField(max_length=2000,null=True)
    ICDScenteraddress = models.CharField(max_length=2000,null=True)
    ICDScontact = models.CharField(max_length=2000,null=True)
    contact=models.CharField(max_length=1000,blank=True)

class AnganwadiWorkersRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,default=False)
    contact=models.CharField(max_length=25500,blank=True)
    ICDSname=  models.CharField(max_length=2000,null=True)
    ICDScenteraddress = models.CharField(max_length=2000,null=True)
    ICDScontact = models.CharField(max_length=2000,null=True)
    
class   SchoolStudentParent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=255,default=False)
    contact=models.CharField(max_length=25500,blank=True)
    schoolname=  models.CharField(max_length=2000)
    personaladdress = models.CharField(max_length=2000,null=True)
    birthdate=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    schooladdress = models.CharField(max_length=2000,null=True)
    schoolcontact=models.CharField(max_length=25500,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    annualincome=models.CharField(choices= annualincome,max_length=25500,blank=True)
    schoolcoordinatorincharge=models.CharField(max_length=25500,blank=True)
    foodhabits=models.CharField(max_length=25500,blank=True,choices = foodhabit)
    profile_photo=models.ImageField( upload_to='SchoolStudentParent/%Y/%m/%d',blank=True)
    contact=models.CharField(max_length=10,blank=True)
    schoolname=  models.CharField(max_length=200)
    personaladdress = models.CharField(max_length=200,null=True)