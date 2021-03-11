

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
# Create your models here.


class AnemicAdolescentGirl(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50)
    birthdate= models.DateField(null=True, blank=True)
    age = models.IntegerField()
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)
    ICDScenteraddress = models.CharField(max_length = 200)
    ICDScentercontact = models.CharField(max_length = 200)
    occupation = models.CharField(choices=occupation,max_length = 100)
    education = models.CharField(choices=education,max_length = 50,null = True)
    annualincome = models.CharField(choices=annualincome,max_length = 50,null = True)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length = 50,choices=unit )
    height = models.IntegerField()
    heightunit = models.CharField(max_length = 50,choices=hgtunit)
    bmi= models.DecimalField(max_digits = 10,decimal_places = 3)
    waist = models.IntegerField(null=True)
    waistunit = models.CharField(max_length=20,choices=hunit)
    hip = models.IntegerField(null=True)
    hipunit = models.CharField(max_length=20,choices=hunit)
    whratio = models.IntegerField(null=True,decimal_places = 3)
    whratioderived = models.IntegerField(null=True)
    foodhabits =  models.CharField(max_length = 20,choices=foodhabit,null = True)
    uploaded_photo = models.ImageField(upload_to='AnemicAdolescentGirl/%Y/%m/%d')
    
    


class AnemicLactatingMother(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50)
    birthdate = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)
    ICDScenteraddress = models.CharField(max_length = 200)
    ICDScentercontact = models.CharField(max_length = 200)
    occupation = models.CharField(choices=occupation,max_length = 100)
    education = models.CharField(choices=education,max_length = 50,null = True)
    annualincome = models.CharField(choices=annualincome,max_length = 50,null = True)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length = 50,choices=unit )
    height = models.IntegerField()
    heightunit = models.CharField(max_length = 50,choices=hgtunit)
    bmi= models.DecimalField(max_digits = 10,decimal_places = 3)
    waist = models.IntegerField(null=True)
    waistunit = models.CharField(max_length=20,choices=hunit)
    hip = models.IntegerField(null=True)
    hipunit = models.CharField(max_length=20,choices=hunit)
    whratio = models.IntegerField(null=True,decimal_places = 3)
    whratioderived = models.IntegerField(null=True)
    foodhabits =  models.CharField(max_length = 20,choices=foodhabit,null = True)
    uploaded_photo = models.ImageField(upload_to='AnemicLactatingMother/%Y/%m/%d')
    
class AnemicPregnantWoman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50)
    birthdate = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)
    ICDScenteraddress = models.CharField(max_length = 200)
    ICDScentercontact = models.CharField(max_length = 200)
    occupation = models.CharField(choices=occupation,max_length = 100)
    education = models.CharField(choices=education,max_length = 50,null = True)
    annualincome = models.CharField(choices=annualincome,max_length = 50,null = True)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length = 50,choices=unit )
    height = models.IntegerField()
    heightunit = models.CharField(max_length = 50,choices=hgtunit)
    bmi= models.DecimalField(max_digits = 10,decimal_places = 3)
    waist = models.IntegerField(null=True)
    waistunit = models.CharField(max_length=20,choices=hunit)
    hip = models.IntegerField(null=True)
    hipunit = models.CharField(max_length=20,choices=hunit)
    whratio = models.IntegerField(null=True,decimal_places = 3)
    whratioderived = models.IntegerField(null=True)
    foodhabits =  models.CharField(max_length = 20,choices=foodhabit,null = True)
    uploaded_photo = models.FileField(upload_to='anemicpregnantwoman/%Y/%m/%d')
    feedback = models.CharField(max_length = 100)


class ProjectManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default = False)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50)
    contact=models.CharField(max_length=10,blank=True)
   
    def __str__(self):
        return self.user.username

class NutritionExpert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default = False)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50)
    contact=models.CharField(max_length=10,blank=True)
class NutriGardenExpert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default = False)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50)
    contact=models.CharField(max_length=10,blank=True)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50)
    contact=models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=200, null=False, blank=False) 
    education = models.CharField(choices=education,max_length = 50,null = True)
   

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=10,blank=True)
    name = models.CharField(max_length=200,null=True)
    institute = models.CharField(choices=Institute,default=False,max_length=20)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid =models.CharField(primary_key=True,max_length=1000)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50, null=True )
    weight = models.IntegerField(default = False)
    weightunit = models.CharField(max_length = 50,choices=unit,default = False )
    height = models.IntegerField(default = False)
    heightunit = models.CharField(max_length = 50,choices= hgtunit,default = False)
    bmi= models.DecimalField(max_digits = 10,decimal_places = 3)
    waist = models.IntegerField(null=True)
    waistunit = models.CharField(max_length=20,choices=hunit)
    hip = models.IntegerField(null=True)
    hipunit = models.CharField(max_length=20,choices=hunit)
    whratio = models.IntegerField(default = 0,decimal_places = 3)
    whratioderived = models.IntegerField(null=True)
    nutrileader = models.CharField(choices=nutirleader,default=False,max_length=20)
    schoolname=  models.CharField(max_length=200,null = True)
    schoolcordinatorincharge=  models.CharField(max_length=200,null = True)
    schooladdress=  models.CharField(max_length=200,null = True)
    schoolcontactinformation=  models.CharField(max_length=200,null = True)
    contact=encrypt(models.CharField(max_length=1000,blank=True))
    uploaded_photo= models.ImageField( upload_to='student/%Y/%m/%d',default = False)
    # personaladdress = models.CharField(max_length=200,null=True)
class bulk_reg(models.Model):
    name= models.CharField( max_length=50)
    mobile= models.CharField(max_length=10)
    birthdate= models.DateField(auto_now=False, auto_now_add=False,null=True)
   

class SMChild(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50)
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)
    ICDScenteraddress = models.CharField(max_length = 200)
    ICDScentercontact = models.CharField(max_length = 200)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length = 50,choices=unit )
    height = models.IntegerField()
    heightunit = models.CharField(max_length = 50,choices=hgtunit)
    bmi= models.DecimalField(max_digits = 10,decimal_places = 3)
    waist = models.IntegerField(null=True)
    waistunit = models.CharField(max_length=20,choices=hunit)
    hip = models.IntegerField(null=True)
    hipunit = models.CharField(max_length=20,choices=hunit)
    whratio = models.IntegerField(null=True,decimal_places = 3)
    whratioderived = models.IntegerField(null=True)
    foodhabits =  models.CharField(max_length = 20,choices=foodhabit,null = True)
    uploaded_photo = models.FileField(upload_to='smchilddocuments/%Y/%m/%d')
  

class SMChildParentsRegister(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    uid = models.CharField(max_length = 50)
    mothername = models.CharField(max_length = 50)
    fathername = models.CharField(max_length = 50)
    motherbirthdate = models.CharField(max_length = 50)
    fatherbirthdate = models.CharField(max_length = 50)
    motherage = models.IntegerField()
    fatherage = models.IntegerField()
    personalcontact = models.CharField(max_length = 200)
    ICDSname = models.CharField(max_length = 200)
    ICDScenteraddress = models.CharField(max_length = 200)
    ICDScentercontact = models.CharField(max_length = 200)
    occupation = models.CharField(choices=occupation,max_length = 100)
    education = models.CharField(choices=education,max_length = 50,null = True)
    annualincome = models.CharField(choices=annualincome,max_length = 50,null = True)
    cuid  = models.CharField(max_length = 10)


class ConcentForm(models.Model):
    concent = models.CharField(max_length = 10)


class PrincipalInvestigators(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default = False)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 50)
   

class WebGISExpert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default = False)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 50)
   
    
class   SchoolCoordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default=False)
    contact=models.CharField(max_length=1000,blank=True)
    schoolname=  models.CharField(max_length=2000)
    personaladdress = models.CharField(max_length=2000,null=True)
    birthdate=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    schooladdress = models.CharField(max_length=2000,null=True)
    schoolcontact=models.CharField(max_length=1000,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    annualincome=models.CharField(choices=annualincome,max_length=1000,blank=True)
    profile_photo=models.ImageField( upload_to='SchoolCoordinator/%Y/%m/%d',blank=True)   

class MukhyaSevika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default=False)
    anganwadinumber = models.IntegerField(default=False)
    contact=models.CharField(max_length=1000,blank=True)
    birthdate=models.DateField(null=True, blank=True)
    age=models.CharField(max_length=200,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    annualincome=models.CharField(choices=annualincome,max_length=1000,blank=True)
    ICDSname=  models.CharField(max_length=2000,null=True)
    ICDScenteraddress = models.CharField(max_length=2000,null=True)
    ICDScontact = models.CharField(max_length=2000,null=True)
    profile_photo=models.ImageField( upload_to='MukhyaSevika/%Y/%m/%d',blank=True)


class AnganwadiWorkersRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default=False)
    contact=models.CharField(max_length=1000,blank=True)
    birthdate=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    annualincome=models.CharField(choices=annualincome,max_length=1000,blank=True)
    anganwadiname = models.CharField(max_length =100,null = True)
    anganwadiaddress = models.CharField(max_length =100,null = True)
    ICDSname=  models.CharField(max_length=2000,null=True)
    ICDScenteraddress = models.CharField(max_length=2000,null=True)
    ICDScontact = models.CharField(max_length=2000,null=True)
    profile_photo=models.ImageField( upload_to='AnganwadiWorker/%Y/%m/%d',blank=True)

class   SchoolStudentParent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length = 50,default=False)
    contact=models.CharField(max_length=1000,blank=True)
    schoolname=  models.CharField(max_length=2000)
    personaladdress = models.CharField(max_length=2000,null=True)
    birthdate=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    schooladdress = models.CharField(max_length=2000,null=True)
    schoolcontact=models.CharField(max_length=1000,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    annualincome=models.CharField(choices= annualincome,max_length=1000,blank=True)
    schoolcoordinatorincharge=models.CharField(max_length=1000,blank=True)
    foodhabits=models.CharField(max_length=1000,blank=True,choices = foodhabit)
    profile_photo=models.ImageField( upload_to='SchoolStudentParent/%Y/%m/%d',blank=True)
    contact=models.CharField(max_length=10,blank=True)
    schoolname=  models.CharField(max_length=200)
    personaladdress = models.CharField(max_length=200,null=True)