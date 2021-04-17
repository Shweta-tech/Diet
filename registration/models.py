

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

sex=[
            ('male', 'male'),
            ('female', 'female'),
    ]
religious=[
    ('Hinduism','Hinduism'),
    ('Islam','Islam'),
    ('Christianity','Christianity'),
    ('Sikhism','Sikhism'),
    ('Jainism','Jainism'),
    ('Buddhism','Buddhism'),
    ('Other','Other'),
]
class NutriInfotainmentSurveyModel(models.Model):
    name_of_volunteer=models.CharField(max_length=255,blank=True)
    name_of_student=models.CharField(max_length=255,blank=True)
    gender=models.CharField(blank=True,choices=sex,max_length=20)
    birthdate=models.DateField(max_length=20,null=True)
    residential_address=models.CharField(max_length=2000,null=True)
    pincode=models.CharField(max_length=10,blank=True)
    name_of_school=models.CharField(max_length=255,blank=True)
    address_of_school=models.CharField(max_length=255,blank=True)
    pincode_of_school=models.CharField(max_length=10,blank=True)
    personal_contact_number=models.CharField(max_length=20,blank=True)
    religion=models.CharField(blank=True,choices=religious,max_length=20)

family=[('My parents','My parents'),
        ('My parents and siblings','My parents and siblings'),
        ('My parents, siblings and grandparents','My parents, siblings and grandparents'),
        ('My parents, siblings, grandparents, aunts, uncles and cousins','My parents, siblings, grandparents, aunts, uncles and cousins'),
        ('Others','Others'),
        ]
edu_guar=[('Professional degree (Post graduate)','Professional degree (Post graduate)'),
        ('Graduate (Bachelors)','Graduate (Bachelors)'),
        ('Higher Secondary certificate (12th Std)','Higher Secondary certificate (12th Std)'),
        ('Secondary school certificate (SSC - 10th Std)','Secondary school certificate (SSC - 10th Std)'),
        ('Middle school (5th to 10th std)','Middle school (5th to 10th std)'),
        ('Primary school (1st to 4th std)','Primary school (1st to 4th std)'),
        ('Illiterate (No education)','Illiterate (No education)'),
        ('Other','Other'),
        ]

income=[('>199,862','>199,862'),
        ('99,931- 199,861','99,931- 199,861'),
        ('74,755 - 99,930','74,755 - 99,930'),
        ('49,962- 74,755','49,962- 74,755'),
        ('29,973- 49,961','29,973- 49,961'),
        ('10,002- 29,972','10,002- 29,972'),
        ('< 10,001','< 10,001'),
        ]
ration=[('Red color','Red color'),
        ('Orange color','Orange color'),
        ('White color','White color'),
        ('No ration card','No ration card'),
]
occu_guar=[
('Accountants','Accountants'),
('Administrative Assistants','Administrative Assistants'), 
('Advocates','Advocates'), 
('Anganwadi Worker','Anganwadi Worker'),
('Architects','Architects'),
('Assemblers','Assemblers'),
('Auditors','Auditors'), 
('Business Person','Business Person'),
('Cleaners (Washing Windows And Other Glass Surfaces Of Buildings)','Cleaners (Washing Windows And Other Glass Surfaces Of Buildings)'), 
('College Principals','College Principals'), 
('Commercial Truck Drivers','Commercial Truck Drivers'), 
('Cooks','Cooks'),
('Craftsmen','Craftsmen'), 
('Crane Operators','Crane Operators'), 
('Doctors','Doctors'), 
('Engineers','Engineers'), 
('Expert Musicians','Expert Musicians'), 
('Farmers','Farmers'), 
('Fishermen','Fishermen'),
('Garbage Collector','Garbage Collector'), 
('General Office Clerks','General Office Clerks'), 
('Housekeeper/ Housemaid (Hotels/ House)','Housekeeper/ Housemaid (Hotels/ House)'), 
('Lecturers','Lecturers'), 
('Mechanist','Mechanist'), 
('Newspaper Editors','Newspaper Editors'), 
('Nurse','Nurse'),
('Office Assistants','Office Assistants'), 
('Paramedics','Paramedics'), 
('Plant And Machine Operators','Plant And Machine Operators'), 
('Plumbers','Plumbers'), 
('Police Officers','Police Officers'), 
('Reading And Emptying Meters','Reading And Emptying Meters'), 
('Receptionists','Receptionists'), 
('Retired','Retired'),
('Salesman','Salesman'), 
('Scientists','Scientists'), 
('Security Guard (Housing Societies/Company/Banks/Land)','Security Guard (Housing Societies/Company/Banks/Land)'), 
('Senior Administrative Officers','Senior Administrative Officers'), 
('Software Development','Software Development'), 
('Soldiers','Soldiers'), 
('Stocking Vending Machines','Stocking Vending Machines'),
('Street Vendor','Street Vendor'), 
('Sweeper','Sweeper'),
('Unemployed','Unemployed'),
('OTHERS','OTHERS'),
]

class NutriSocioDemographicModel(models.Model):
    i_live_with=models.CharField(blank=True,choices=family,max_length=100)
    number_of_family_members=models.CharField(blank=True,max_length=100)
    name_of_the_guardian=models.CharField(blank=True,max_length=100)
    age_of_the_guardian=models.CharField(blank=True,max_length=100)
    education_of_the_guardian=models.CharField(blank=True,max_length=100,choices=edu_guar)
    occupation_of_the_guardian=models.CharField(blank=True,max_length=300,choices=occu_guar)
    monthly_family_income=models.CharField(blank=True,max_length=100,choices=income)
    ration_card_color_is=models.CharField(blank=True,max_length=100,choices=ration)

class NutriAnthropometricParametersModel(models.Model):
    Enter_your_weight=models.CharField(blank=True,max_length=100)
    Enter_your_height=models.CharField(blank=True,max_length=100)
    Enter_your_waist_circumference=models.CharField(blank=True,max_length=100)
    Enter_your_hip_circumference=models.CharField(blank=True,max_length=100)

dietary_habit=[
    ('Please select:','Please select:'),
    ('I eat only vegetables. I DO NOT eat milk, eggs, chiken, mutton or fish. (Vegan)','I eat only vegetables. I DO NOT eat milk, eggs, chiken, mutton or fish. (Vegan)'),
    ('I eat only milk and vegetables. I DO NOT eat eggs, chicken, mutton, fish. (Lacto-Vegetarian)','I eat only milk and vegetables. I DO NOT eat eggs, chicken, mutton, fish. (Lacto-Vegetarian)'),
    ('I eat only eggs and vegetables. I DO NOT eat milk, chicken, mutton or fish. (Eggetarian)','I eat only eggs and vegetables. I DO NOT eat milk, chicken, mutton or fish. (Eggetarian)'),
    ('I eat milk, eggs and vegetables. I DO NOT eat chicken, mutton, fish.(Lacto-ova-vegetarian)','I eat milk, eggs and vegetables. I DO NOT eat chicken, mutton, fish.(Lacto-ova-vegetarian)'),
    ('I eat vegetables, milk, egg, chicken, mutton, fish. (Non-vegetarian)','I eat vegetables, milk, egg, chicken, mutton, fish. (Non-vegetarian)'),
    ('I eat vegetables, milk and fish. I DO NOT eat eggs, chicken and mutton. (Pescatarian)','I eat vegetables, milk and fish. I DO NOT eat eggs, chicken and mutton. (Pescatarian)'),
]

meal_time=[
    ('Breakfast','Breakfast'),
    ('Mid-morning snack','Mid-morning snack'),
    ('Lunch','Lunch'),
    ('Afternoon snack','Afternoon snack'),
    ('Evening snack','Evening snack'),
    ('Dinner','Dinner'),
    ('Bed-time snack','Bed-time snack'),
    ('Other','Other'),
]
tiffin_ch=[
    ('Please select:','Please select:'),
    ('I carry my tiffin daily','I carry my tiffin daily'),
    ('I carry my tiffin only once a week','I carry my tiffin only once a week'),
    ('I carry my tiffin 2-3 times a week','I carry my tiffin 2-3 times a week'),
    ('I carry my tiffin more than 3 times a week','I carry my tiffin more than 3 times a week'),
    ('I never carry my tiffin','I never carry my tiffin'),
]
midday_meal_ch=[
    ('Please select:','Please select:'),
    ('Yes, I get it and I love it','Yes, I get it and I love it'),
    ('Yes, I get it but I dont Like it so I eat something else','Yes, I get it but I dont Like it so I eat something else'),
    ('No, I dont get Mid-day meal in my school','No, I dont get Mid-day meal in my school'),
]
soyabean_ch=[
    ('Please select:','Please select:'),
    ('Daily','Daily'),
    ('Thrice in a week','Thrice in a week'),
    ('Once in a week','Once in a week'),
    ('Twice in a month','Twice in a month'),
    ('Monthly','Monthly'),
    ('Never','Never'),
]
# binary=[
#     ('yes','yes'),
#     ('no','no'),
# ]
yesno=[
    ('yes','yes'),
    ('no','no'),
]
class FoodHabitsModel(models.Model):
    Choose_your_dietary_habit=models.CharField(blank=True,max_length=100,choices=dietary_habit)
    #Choose_meals_consumed_in_a_day=models.CharField(blank=True,max_length=100,choices=meal_time)
    Choose_meals_consumed_in_a_day=MultiSelectField(blank=True,choices=meal_time)
    other_meal=models.CharField(blank=True,max_length=1000)
    breakfast=models.CharField(blank=True,max_length=1000)
    lunch=models.CharField(blank=True,max_length=1000)
    dinner=models.CharField(blank=True,max_length=1000)
    snack=models.CharField(blank=True,max_length=1000)
    canteen=models.CharField(blank=True,max_length=1000)
    tiffin=models.CharField(blank=True,max_length=100,choices=tiffin_ch)
    midday_meal=models.CharField(blank=True,max_length=100,choices=midday_meal_ch)
    soyabean=models.CharField(blank=True,max_length=100,choices=soyabean_ch)
    bananapeel=models.CharField(blank=True,max_length=100,choices=yesno)
    bottlegourd=models.CharField(blank=True,max_length=100,choices=yesno)
    



