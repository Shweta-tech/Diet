from django import forms  
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
import random
from multiselectfield import MultiSelectField
import string
from django.forms import Textarea
<<<<<<< HEAD
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from .models import Mentor,MukhyaSevika,AnganwadiWorkersRegister,Student,SchoolCoordinator,User,AnemicPregnantWoman,SMChildParentsRegister,ConcentForm,NutriGardenExpert,AnemicLactatingMother,AnemicAdolescentGirl,SMChild,SchoolStudentParent,NutriInfotainmentSurveyModel,NutriSocioDemographicModel,NutriAnthropometricParametersModel,FoodHabitsModel
=======
from bootstrap_datepicker_plus import DatePickerInput
from .models import Mentor,MukhyaSevika,AnganwadiWorkersRegister,Student,SchoolCoordinator,User,AnemicPregnantWoman,SMChildParentsRegister,ConcentForm,NutriGardenExpert,AnemicLactatingMother,anemicadolescentgirl,SMChild,SchoolStudentParent
>>>>>>> 97f532dadca856a2f108235854001be68d4cbc17
class Form(UserCreationForm):
    email=forms.EmailField(required=False)
    first_name=forms.CharField(max_length=255)
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
    


        

class MentorForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='MT'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = Mentor
        fields = ('contact','uid')


class SchoolCoordinatorForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SCU'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))

    class Meta:
        model = SchoolCoordinator
        fields = ('contact','position','schoolname','schoolcontact','uid')
        # widgets = {
        #             'birthdate': DatePickerInput(format='%m/%d/%Y'), 
        #          }


class StudentForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='STU'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    # weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    # weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    # height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    # heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    # waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    # waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    # hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    # hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    # contact=forms.CharField(required=True)
    class Meta:
        model = Student
        fields = ('nutrileader','uid','contact',)

class AnganwadiWorkerForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='ANW'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = AnganwadiWorkersRegister
        fields = ('contact','ICDSname','ICDScenteraddress','ICDScontact','uid')
        # widgets = {
        #             'birthdate': DatePickerInput(format='%Y/%m/%d'),
        #          }
        
class MukhyaSevikaForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='MSU'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = MukhyaSevika
        fields = ('contact','ICDSname','ICDScenteraddress','ICDScontact','uid')

        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class SchoolStudentParentForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='STUP'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    class Meta:
        model = SchoolStudentParent
        fields = ('contact','schoolname','personaladdress','birthdate','age','schooladdress','schoolcontact','education','occupation','annualincome','schoolcoordinatorincharge','foodhabits','profile_photo','uid')
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }

class AnemicLactatingMotherForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='ALM'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
  
    class Meta:
        model = AnemicLactatingMother
        fields =   ['personalcontact','childbirthdate','ICDSname','uid']
        widgets = {
                    'childbirthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }
class anemicadolescentgirlForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='AAG'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = anemicadolescentgirl
        fields = ['personalcontact','ICDSname','uid']

        
class AnemicPregnantWomanForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='APW'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    class Meta:
        model = AnemicPregnantWoman
        fields =  ['personalcontact','ICDSname','trimester','uid']
        

class SMChildForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SMC'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    weight=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    weightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in kgs/lbs'}))
    height=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass'}))
    heightunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'bmicalculateclass','placeholder':'in feet/inches/cms/meters'}))
    waist=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    waistunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    hip=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass'}))
    hipunit=forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','class':'whratiocalculateclass','placeholder':'in cms/inches'}))
    class Meta:
        model = SMChild
        fields = ['birthdate','age','personalcontact','ICDSname','ICDScenteraddress','ICDScentercontact','weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio','whratioderived','foodhabits','uploaded_photo','uid']
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                  
        }


class SMChildParentsRegisterForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SMP'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
  
    class Meta:
        model = SMChildParentsRegister
        fields =  ['personalcontact','ICDSname','childis','childfirstname','childlastname','childbirthdate','uid'] 
        widgets = {
                        'childbirthdate': DatePickerInput(format='%m/%d/%Y'), 
        }

class ConcentForm(forms.ModelForm):
    class Meta:
        model = ConcentForm
        fields = ['concent']
class NutriGardenExpertForm(forms.ModelForm):
    uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='NGE'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
    # birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))

    class Meta:
        model = NutriGardenExpert
        fields = ['contact','uid']
        # widgets = {
        #             'birthdate': DatePickerInput(format='%m/%d/%Y'), # default date-format %m/%d/%Y will be used
            
        # }
            
        
class NutriInfotainmentSurveyForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    # name_vol = forms.ChoiceField(label='Name of the volunteer (by whom the details are filled)')
    # name_stu=forms.ChoiceField(label='School student name (age 10-15 years)')
    # address=forms.ChoiceField(label='My residential address')
    # pincode=forms.ChoiceField(label='Pincode of residential address')
    class Meta:
        model=NutriInfotainmentSurveyModel
        fields="__all__"
        widgets = {
                    'birthdate': DatePickerInput(format='%Y/%m/%d'), 
                  
        }
class NutriSocioDemographicForm(forms.ModelForm):
    class Meta:
        model=NutriSocioDemographicModel
        fields="__all__"
        widgets={
            'i_live_with':forms.Select(attrs={'class':'form-control'}),
            'number_of_family_members':forms.TextInput(attrs={'class':'form-control'}),
            'name_of_the_guardian':forms.TextInput(attrs={'class':'form-control','placeholder':'Write the name and relation between you and your parent/care-taker/guardian e.g. Ram (father)'}),
            'age_of_the_guardian':forms.TextInput(attrs={'class':'form-control'}),
            'education_of_the_guardian':forms.Select(attrs={'class':'form-control'}),
            'occupation_of_the_guardian':forms.Select(attrs={'class':'form-control'}),
            'monthly_family_income':forms.Select(attrs={'class':'form-control','placeholder':'in Rupees'}),
            'ration_card_color_is':forms.Select(attrs={'class':'form-control'}),
        }

class NutriAnthropometricParametersForm(forms.ModelForm):
    class Meta:
        model=NutriAnthropometricParametersModel
        fields="__all__"
        widgets={
            'Enter_your_weight':forms.TextInput(attrs={'class':'form-control','placeholder':'in kgs'}),
            'Enter_your_height':forms.TextInput(attrs={'class':'form-control','placeholder':'in cms'}),
            'Enter_your_waist_circumference':forms.TextInput(attrs={'class':'form-control','placeholder':'in cms'}),
            'Enter_your_hip_circumference':forms.TextInput(attrs={'class':'form-control','placeholder':'in cms'}),
        }

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
class FoodHabitsForm(forms.ModelForm):
    Choose_your_dietary_habit=forms.ChoiceField(choices=dietary_habit,widget=forms.Select(attrs={'class':'form-control'}))
    #Choose_meals_consumed_in_a_day=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=meal_time)
    other_meal=forms.CharField(label="Meals if had, other than the above list, add them here (Please write the food consumed and amount as per household cutlery)",widget=forms.Textarea(attrs={'class':'form-control','class': 'no-bullet-list','list-style-type':'none;'}))
    breakfast=forms.CharField(label="What did you have for breakfast yesterday & How much? (Please write the food consumed and amount as per household cutlery)",widget=forms.Textarea(attrs={'class':'form-control'}))
    lunch=forms.CharField(label="What did you have for lunch yesterday & How much? (Please write the food consumed and amount as per household cutlery)",widget=forms.Textarea(attrs={'class':'form-control'}))
    dinner=forms.CharField(label="What did you have for dinner yesterday & How much? (Please write the food consumed and amount as per household cutlery)",widget=forms.Textarea(attrs={'class':'form-control'}))
    snack=forms.CharField(label="What did you have for snacks yesterday & How much? (Please write the food consumed and amount as per household cutlery)",widget=forms.Textarea(attrs={'class':'form-control'}))
    canteen=forms.CharField(label="Does your school have a canteen? If yes please mention what you would eat from your canteen. If no please write No below.",widget=forms.Textarea(attrs={'class':'form-control'}))
    #widget=forms.Textarea(attrs={"rows":10, "cols":80})
    tiffin=forms.ChoiceField(label="Before the lockdown, when you went to the school, how often did you carry Tiffin?",choices=tiffin_ch,widget=forms.Select(attrs={'class':'form-control'}))
    midday_meal=forms.ChoiceField(label="Did you get a Mid-day meal in your school before the lockdown?",choices=midday_meal_ch,widget=forms.Select(attrs={'class':'form-control'}))
    soyabean=forms.ChoiceField(label="How frequently do you eat soya bean e.g. soya milk, soya bean, tofu etc ?",choices=soyabean_ch,widget=forms.Select(attrs={'class':'form-control'}))
    bananapeel=forms.ChoiceField(label="Do you consume banana peel?",choices=yesno,widget=forms.RadioSelect())
    bottlegourd=forms.ChoiceField(label="Do you consume bottle gourd (dudhi/lauki) peel?",choices=yesno,widget=forms.RadioSelect())
    #attrs={'class':'form-control'}
    class Meta:
        model=FoodHabitsModel
        fields="__all__"
