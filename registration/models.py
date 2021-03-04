

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
nutirleader = [
    ('Nutri-Leader','Nutri-Leader'),
    ('School-Student','School-Student')
]
fatheroccupation = [('Legislators,Senior Officials & Managers','Legislators,Senior Officials & Managers'),
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

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=10,blank=True)
    name = models.CharField(max_length=200,null=True)
    institute = models.CharField(choices=Institute,default=False,max_length=20)
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid =models.CharField(primary_key=True,max_length=100)
    nutrileader = models.CharField(choices=nutirleader,default=False,max_length=20)
    contact=encrypt(models.CharField(max_length=1000,blank=True))
    # personaladdress = models.CharField(max_length=200,null=True)
class bulk_reg(models.Model):
    name= models.CharField( max_length=50)
    mobile= models.CharField(max_length=10)
    dob= models.DateField(auto_now=False, auto_now_add=False,null=True)

class MukhyaSevika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    anganwadinumber = models.IntegerField(default=False)

class MukhyaSevikaProfile(models.Model):
    name = models.CharField(max_length = 100,blank = True)
    contact=models.CharField(max_length=10,blank=True)
    dob = models.DateField(default=datetime.now, blank=True)
    age= models.CharField(max_length=6,null = True,default = 0)
    age_in_months= models.CharField(max_length=6,null = True,default = 0)
    age_in_days= models.CharField(max_length=6,null = True,default=0)
    personaladdress = models.CharField(max_length=200,null = True)
    uploaded_image = models.ImageField( upload_to='mukhyasevikaid/%Y/%m/%d')

class AnganwadiWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    anganwadiname = models.CharField(max_length=200, null=True)
    anganwadiaddress = models.CharField(max_length=200,null=True)

class AnganwadiWorkerProfile(models.Model):
    name = models.CharField(max_length = 100)
    dob = models.DateField(default=datetime.now)
    age= models.CharField(max_length=6,)
    age_in_months= models.CharField(max_length=6)
    age_in_days= models.CharField(max_length=6)
    contact=models.CharField(max_length=10)
    personaladdress = models.CharField(max_length=200)
    uploaded_image = models.ImageField( upload_to='anganwadiworkerid/%Y/%m/%d')


class SMChildParentsRegister(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    cuid  = models.CharField(max_length = 10)

class SMChildParentsDetails(models.Model):
    mothername = models.CharField(max_length = 50)
    fathername = models.CharField(max_length = 50)
    motherage = models.IntegerField()
    fatherage = models.IntegerField()
    fatheroccupation = models.CharField(choices=fatheroccupation,max_length = 100)
    education = models.CharField(choices=education,max_length = 50,null = True)
    monthlyincome = models.CharField(choices=monthlyincome,max_length = 50)


class NutriGardenExpert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,blank=True)
class ConcentForm(models.Model):
    concent = models.CharField(max_length = 10)


class AdolescentAnemicGirl(models.Model):
    uniqueid = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length = 50)
    height = models.IntegerField()
    heightunit = models.CharField(max_length = 50)
    bmi= models.DecimalField(max_digits = 5,decimal_places = 2)
    age = models.IntegerField()
    hemoglobinvalue = models.IntegerField()
    hemoglobindate = models.DateField(default=datetime.now, blank=True)
    food = models.CharField(max_length = 50)
    complication = models.CharField(max_length = 50)
    education= models.CharField(max_length = 50)
    medication = models.CharField(max_length = 50)
    health = models.CharField(max_length = 50)
    medical= models.CharField(max_length = 50)
    uploaded_file = models.FileField(upload_to='adolescentgirldocuments/%Y/%m/%d')
    feedback = models.CharField(max_length = 100)

class PregnantWoman(models.Model):
    uniqueid = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length = 50)
    height = models.IntegerField()
    heightunit = models.CharField(max_length = 50)
    bmi= models.DecimalField(max_digits = 5,decimal_places = 2)
    age = models.IntegerField()
    hemoglobinvalue = models.IntegerField()
    hemoglobindate = models.DateField(default=datetime.now, blank=True)
    food = models.CharField(max_length = 50, blank=True)
    complication = models.CharField(max_length = 50)
    medication = models.CharField(max_length = 50)
    health = models.CharField(max_length = 50, blank = True)
    medical= models.CharField(max_length = 50)
    uploaded_file = models.FileField(upload_to='pregnantwomandocuments/%Y/%m/%d')
    feedback = models.CharField(max_length = 100)


class SMChildDetails(models.Model):
    uniqueid = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length = 50)
    height = models.IntegerField()
    heightunit = models.CharField(max_length = 50)
    bmi= models.DecimalField(max_digits = 5,decimal_places = 2)
    age = models.IntegerField()
    hemoglobinvalue = models.IntegerField()
    hemoglobindate = models.DateField(default=datetime.now, blank=True)
    food = models.CharField(max_length = 50, blank=True)
    complication = models.CharField(max_length = 50)
    education= models.CharField(max_length = 50, blank = True)
    medication = models.CharField(max_length = 50)
    health = models.CharField(max_length = 50, blank = True)
    medical= models.CharField(max_length = 50)
    uploaded_file = models.FileField(upload_to='smchilddocuments/%Y/%m/%d')
    feedback = models.CharField(max_length = 100)
