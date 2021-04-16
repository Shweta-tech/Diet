from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from registration.models import Student,Mentor,SchoolCoordinator,MukhyaSevika,AnganwadiWorkersRegister
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
unit = [('kgs','kgs'),('lbs','lbs')]
hunit = [('cms','cms'),('inches','inches')]
hgtunit = [ ('feet','feet'), ('inches','inches'),('cms','cms'),('inches','inches')]
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
class studentprof(models.Model):
    user = models.OneToOneField(Student, on_delete = models.CASCADE)
    uid=models.CharField(max_length=100,null=True)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length = 50, null=True )
    # weight = models.IntegerField(default = False)
    # weightunit = models.CharField(max_length=255,choices=unit,default = False )
    # height = models.IntegerField(default = False)
    # heightunit = models.CharField(max_length = 50,choices= hgtunit,default = False)
    # bmi= models.DecimalField(max_digits = 10,decimal_places = 3)
    # waist = models.IntegerField(null=True)
    # waistunit = models.CharField(max_length=20,choices=hunit)
    # hip = models.IntegerField(null=True)
    # hipunit = models.CharField(max_length=20,choices=hunit)
    # whratio = models.DecimalField(max_digits = 10,default = 0,null=True,decimal_places = 3)
    # whratioderived = models.IntegerField(null=True)
    schoolname=  models.CharField(max_length=200,null = True)
    schoolcordinatorincharge=  models.CharField(max_length=200,null = True)
    schooladdress=  models.CharField(max_length=200,null = True)
    schoolcontactinformation=  models.CharField(max_length=200,null = True)
    uploaded_photo= models.ImageField( upload_to='student/%Y/%m/%d',default = False)
    personaladdress = models.CharField(max_length=200,null=True)
class ngprof(models.Model):
    user = models.OneToOneField(Mentor, on_delete = models.CASCADE)
    uid=models.CharField(max_length=100,null=True)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=255)

class scprof(models.Model):
    user = models.OneToOneField(SchoolCoordinator, on_delete = models.CASCADE)
    uid=models.CharField(max_length=100,null=True)
    personaladdress = models.CharField(max_length=2000,null=True)
    birthdate=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    schooladdress = models.CharField(max_length=2000,null=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    annualincome=models.CharField(choices=annualincome,max_length=25500,blank=True)
    profile_photo=models.ImageField( upload_to='SchoolCoordinator/%Y/%m/%d',blank=True)   

class mentorprof(models.Model):
    user = models.OneToOneField(Mentor, on_delete = models.CASCADE)
    uid=models.CharField(max_length=100,null=True)
    birthdate = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=255)
    address = models.CharField(max_length=200, null=False, blank=False) 
    education = models.CharField(choices=education,max_length=255,null = True)
class PersonalInformationForms(models.Model):
    uniqueid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    days = models.CharField(max_length=2)
    fathername = models.CharField(max_length=200)
    mothername = models.CharField(max_length=200)
    contactnumber = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=2000)
    profileimage = models.ImageField( upload_to='profileimages/%Y/%m/%d')

class msprof(models.Model):
    user = models.OneToOneField(MukhyaSevika, on_delete = models.CASCADE)
    uid=models.CharField(max_length=100,null=True)
    anganwadinumber = models.IntegerField(default=False)
    birthdate=models.DateField(null=True, blank=True)
    age=models.CharField(max_length=200,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    annualincome=models.CharField(choices=annualincome,max_length=25500,blank=True)
    profile_photo=models.ImageField( upload_to='MukhyaSevika/%Y/%m/%d',blank=True)
class awprof(models.Model):
    user = models.OneToOneField(AnganwadiWorkersRegister, on_delete = models.CASCADE)
    uid=models.CharField(max_length=100,null=True)
    birthdate=models.CharField(max_length=2000,null=True)
    age=models.CharField(max_length=200,blank=True)
    education=models.CharField(choices=education,max_length=2000,blank=True)
    occupation=models.CharField(choices=occupation,max_length=2000,blank=True)
    annualincome=models.CharField(choices=annualincome,max_length=25500,blank=True)
    anganwadiname = models.CharField(max_length=255,null = True)
    anganwadiaddress = models.CharField(max_length=255,null = True)
    profile_photo=models.ImageField( upload_to='AnganwadiWorker/%Y/%m/%d',blank=True)

class DailyScheduleForm(models.Model):
    user = models.OneToOneField(PersonalInformationForms, on_delete = models.CASCADE)
    activity=models.CharField(max_length=100,null=True)
    sleepfrom = models.TimeField(null=True)
    sleepto = models.TimeField(null=True)
    eatfrom = models.TimeField(null=True)
    eatto = models.TimeField(null=True)
    studyfrom = models.TimeField(null=True)
    studyto = models.TimeField(null=True)
    playfrom = models.TimeField(null=True)
    playto = models.TimeField(null=True)
    housework  = models.CharField(max_length=500)
    activities = models.CharField(max_length=500)

class BodyModel(models.Model):
    user = models.OneToOneField(DailyScheduleForm, on_delete = models.CASCADE)
    weight = models.IntegerField(null=True)
    weightunit = models.CharField(max_length=20)
    height = models.IntegerField(null=True)
    heightunit = models.CharField(max_length=20)
    bmi = models.IntegerField(null=True)
    waist = models.IntegerField(null=True)
    waistunit = models.CharField(max_length=20)
    hip = models.IntegerField(null=True)
    hipunit = models.CharField(max_length=20)
    whratio = models.IntegerField(null=True)

class EatTodayModel(models.Model):
    user = models.OneToOneField(BodyModel, on_delete = models.CASCADE)
    foodhabbits = models.CharField(max_length=200)
    foodallergies = models.CharField(max_length=200)

class DietModel(models.Model):
    user = models.OneToOneField(EatTodayModel, on_delete = models.CASCADE)
    mealtype = models.CharField(max_length=200)
    timefrom = models.TimeField()
    timeto = models.TimeField()
    recipe=models.CharField(max_length=100,null=True)
    rotiquantity = models.IntegerField(default = 0,blank=True,null = True)
    rotiunit = models.CharField(max_length=200,blank=True,null = True)
    ricequantity = models.IntegerField(default = 0,blank=True,null = True)
    riceunit  = models.CharField(max_length=200,blank=True,null = True)
    pohaquantity = models.IntegerField(default = 0,blank=True,null = True)
    pohaunit  = models.CharField(max_length=200,blank=True,null = True)
    upmaquantity = models.IntegerField(default = 0,blank=True,null = True)
    upmaunit  = models.CharField(max_length=200,blank=True,null = True)
    teaquantity = models.IntegerField(default = 0,blank=True,null = True)
    teaunit  = models.CharField(max_length=200,blank=True,null = True)
    coffeequantity = models.IntegerField(default = 0,blank=True,null = True)
    coffeeunit  = models.CharField(max_length=200,blank=True,null = True)
    milkquantity = models.IntegerField(default = 0,blank=True,null = True)
    milkunit  = models.CharField(max_length=200,blank=True,null = True)
    vadaquantity = models.IntegerField(default = 0,blank=True,null = True)
    biscuitquantity = models.IntegerField(default = 0,blank=True,null = True)
    dalquantity = models.IntegerField(default = 0,blank=True,null = True)
    dalunit  = models.CharField(max_length=200,blank=True,null = True)
    gujratidalquantity = models.IntegerField(default = 0,blank=True,null = True)
    gujratidalunit  = models.CharField(max_length=200,blank=True,null = True)
    toordalquantity = models.IntegerField(default = 0,blank=True,null = True)
    toordalunit  = models.CharField(max_length=200,blank=True,null = True)
    moongdalquantity = models.IntegerField(default = 0,blank=True,null = True)
    moongdalunit  = models.CharField(max_length=200,blank=True,null = True)
    palakquantity = models.IntegerField(default = 0,blank=True,null = True)
    palakunit  = models.CharField(max_length=200,blank=True,null = True)





class FeedbackModel(models.Model):
    name = models.CharField(max_length = 100)
    issues = models.TextField(max_length = 2000)
    suggestions = models.TextField(max_length  = 2000)

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

# class DietRecallModel(models.Model):
#     uid = models.CharField(max_length=255,default=False)
#     eathabit=models.CharField(max_length=200,default=False)
#     # TIMING TABLE
#     glasseswater=models.CharField(max_length=200,default=False)
#     # FOOD ITEM TABLE
#     foodtime=models.CharField(max_length=200,default=False)
#     beforelock=models.CharField(max_length=200,default=False)
#     middaymeal=models.CharField(max_length=200,default=False) #add typing choice
#     # MANY TABLES