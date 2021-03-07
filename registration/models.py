

# Create your models here.
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string
from datetime import datetime 
from django_cryptography.fields import encrypt
from uuid import UUID
from fernet_fields import EncryptedTextField

MentorType = [
        ('Head Mentor', 'Head Mentor'),
        ('Support Mentor', 'Support Mentor'),

]

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
nutrileader = [
    ('Nutri-Leader','Nutri-Leader'),
    ('School-Student','School-Student')
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
monthlyincome =  [ ('199,862','199,862'),
    ('99,931-199,861','99,931-199,861'),
    ('74,755-99,930','74,755-99,930'),
    ('49,962-74,755','49,962-74,755'),
    ('29,973-49,961','29,973-49,961'),
    ('10,002-29,97','10,002-29,97'),
    ('10,001','10,001'),
]

# Create your models here.
class AdolescentGirlRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid =models.CharField(primary_key=True,max_length=100)
    contact=models.CharField(max_length=10,blank=True)

class AnemicWomanRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid =models.CharField(primary_key=True,max_length=100)
    contact=models.CharField(max_length=10,blank=True)

class PregnantWomanRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid =models.CharField(primary_key=True,max_length=100)
    contact=models.CharField(max_length=10,blank=True)


class ProjectCoordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,blank=True)

class ProjectManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.user.username
class TechnicalExpert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=10,blank=True)

class HeadMentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=200, null=False, blank=False) 
    mentortype = models.CharField(choices=MentorType,default=False,max_length=20)
    institute = models.CharField(choices =Institute,default = False,max_length =20)
    qualification = models.CharField(choices=Qualification,default=False,max_length=10)

class SupportMentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=10,blank=True)
    mentortype = models.CharField(choices=MentorType,default=False,max_length=20)
    category = models.CharField(choices=Category,default=False,max_length=20)

class   SchoolCoordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=1000,blank=True)
    schoolname=  models.CharField(max_length=2000)
    personaladdress = models.CharField(max_length=2000,null=True)
    dob=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    schooladdress = models.CharField(max_length=2000,null=True)
    schoolcontact=models.CharField(max_length=1000,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    monthlyincome=models.CharField(choices=monthlyincome,max_length=1000,blank=True)
    profilephoto=models.ImageField( upload_to='images/%Y/%m/%d',blank=True)

class   SchoolStudentParent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=1000,blank=True)
    schoolname=  models.CharField(max_length=2000)
    personaladdress = models.CharField(max_length=2000,null=True)
    dob=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    schooladdress = models.CharField(max_length=2000,null=True)
    schoolcontact=models.CharField(max_length=1000,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    monthlyincome=models.CharField(choices=monthlyincome,max_length=1000,blank=True)
    schoolcoordinatorincharge=models.CharField(max_length=1000,blank=True)
    foodhabits=models.CharField(max_length=1000,blank=True)
    profilephoto=models.ImageField( upload_to='images/%Y/%m/%d',blank=True)


class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=10,blank=True)
    name = models.CharField(max_length=200,null=True)
    institute = models.CharField(choices=Institute,default=False,max_length=20)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid =models.CharField(primary_key=True,max_length=100)
    nutrileader = models.CharField(choices=nutrileader,default=False,max_length=20)
    contact=encrypt(models.CharField(max_length=1000,blank=True))
    # personaladdress = models.CharField(max_length=200,null=True)
class bulk_reg(models.Model):
    name= models.CharField( max_length=50)
    mobile= models.CharField(max_length=10)
    dob= models.DateField(auto_now=False, auto_now_add=False,null=True)

class MukhyaSevika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    anganwadinumber = models.IntegerField(default=False)
    contact=models.CharField(max_length=1000,blank=True)
    dob=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    monthlyincome=models.CharField(choices=monthlyincome,max_length=1000,blank=True)
    ICDSname=  models.CharField(max_length=2000,null=True)
    ICDScenteraddress = models.CharField(max_length=2000,null=True)
    ICDScontact = models.CharField(max_length=2000,null=True)
    profilephoto=models.ImageField( upload_to='images/%Y/%m/%d',blank=True) 

class AnganwadiWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    anganwadiname = models.CharField(max_length=200, null=True)
    anganwadiaddress = models.CharField(max_length=200,null=True)
    contact=models.CharField(max_length=1000,blank=True)
    dob=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    monthlyincome=models.CharField(choices=monthlyincome,max_length=1000,blank=True)
    ICDSname=  models.CharField(max_length=2000,null=True)
    ICDScenteraddress = models.CharField(max_length=2000,null=True)
    ICDScontact = models.CharField(max_length=2000,null=True)
    profilephoto=models.ImageField( upload_to='images/%Y/%m/%d',blank=True)    

class SMChildParentsRegister(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    cuid  = models.CharField(max_length = 10)
    
class NutriGardenExpert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,blank=True)
class ConcentForm(models.Model):
    concent = models.CharField(max_length = 10)


