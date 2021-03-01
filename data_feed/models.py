from django.db import models

# Create your models here.
class PersonalInformationForms(models.Model):
    uniqueid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    days = models.CharField(max_length=2)
    fathername = models.CharField(max_length=200)
    mothername = models.CharField(max_length=200)
    contactnumber = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    profileimage = models.ImageField( upload_to='profileimages/%Y/%m/%d')
   

class DailyScheduleForm(models.Model):
    sleepfrom = models.TimeField()
    sleepto = models.TimeField()
    eatfrom = models.TimeField()
    eatto = models.TimeField()
    studyfrom = models.TimeField()
    studyto = models.TimeField()
    playfrom = models.TimeField()
    playto = models.TimeField()
    housework  = models.CharField(max_length=500)
    activities = models.CharField(max_length=500)

class BodyModel(models.Model):
    weight = models.IntegerField()
    weightunit = models.CharField(max_length=20)
    height = models.IntegerField()
    heightunit = models.CharField(max_length=20)
    bmi = models.IntegerField()
    waist = models.IntegerField()
    waistunit = models.CharField(max_length=20)
    hip = models.IntegerField()
    hipunit = models.CharField(max_length=20)
    whratio = models.IntegerField()

class DietModel(models.Model):
    mealtype = models.CharField(max_length=200)
    timefrom = models.TimeField()
    timeto = models.TimeField()
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

class EatTodayModel(models.Model):
    foodhabbits = models.CharField(max_length=200)
    foodallergies = models.CharField(max_length=200)





class FeedbackModel(models.Model):
    name = models.CharField(max_length = 100)
    issues = models.TextField(max_length = 2000)
    suggestions = models.TextField(max_length  = 2000)

class AdolescentGirlsModel(models.Model):
    uid = models.CharField(max_length = 100)
    name = models.CharField(max_length = 2000)
    weight = models.IntegerField()
    weightunit = models.CharField(max_length=20)
    height = models.IntegerField()
    heightunit = models.CharField(max_length=20)
    bmi = models.IntegerField()
    age = models.IntegerField()
    hemoglobinvalue = models.DecimalField(decimal_places  =2 , max_digits = 4)
    date = models.DateField()
    recommendedfood = models.CharField(max_length = 2000)
    complication = models.CharField(max_length = 2000)
    education = models.CharField(max_length = 2000)
    medication = models.CharField(max_length = 2000)
    healthparameters = models.CharField(max_length = 2000)
    medicaladvice = models.CharField(max_length = 2000)
    uploaddocuments = models.FileField(upload_to='documents/%Y/%m/%d')
    deedback = models.CharField(max_length = 2000)
