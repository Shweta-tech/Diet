

# Create your models here.
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

# Create your models here.
class AdolescentGirlRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,blank=True)

class AnemicWomanRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,blank=True)

class PregnantWomanRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,blank=True)

class SMMotherRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    contact=encrypt(models.CharField(max_length=1000,blank=True))
    # personaladdress = models.CharField(max_length=200,null=True)
class bulk_reg(models.Model):
    name= models.CharField( max_length=50)
    mobile= models.CharField(max_length=10)
    dob= models.DateField(auto_now=False, auto_now_add=False,null=True)
class AnganwadiWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=10,blank=True)
    anganwadiname = models.CharField(max_length=200, null=True)
    personaladdress = models.CharField(max_length=200,null=True)
    anganwadiaddress = models.CharField(max_length=200,null=True)

class MukhyaSevika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    contact=models.CharField(max_length=10,blank=True)
    personaladdress = models.CharField(max_length=200,null = True)
    anganwadinumber = models.IntegerField(default=False)