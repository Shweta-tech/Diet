from django import forms  
from datetimepicker.widgets import DateTimePicker
from bootstrap_datepicker_plus import DatePickerInput

from django.contrib.auth.forms import UserCreationForm
import random
import string
from django.forms import Textarea
from .models import DailyScheduleForm,BodyModel,EatTodayModel,DietModel,FeedbackModel,studentprof,ngprof,msprof,awprof,mentorprof,scprof

eathabit_c=[
                ('I eat only vegetables. I DO NOT eat milk, eggs, chiken, mutton or fish (Vegan)','I eat only vegetables. I DO NOT eat milk, eggs, chiken, mutton or fish (Vegan)'),
                ('I eat only Milk and vegetables. I DO NOT eat eggs, chicken, mutton, fish (lacto- vegetarian)','I eat only Milk and vegetables. I DO NOT eat eggs, chicken, mutton, fish (lacto- vegetarian)'),
                ('I eat Only eggs and vegetables. I DO NOT eat milk, chicken, mutton or fish (Eggetarian)','I eat Only eggs and vegetables. I DO NOT eat milk, chicken, mutton or fish (Eggetarian)'),
                ('I eat milk, eggs and vegetables. I DO NOT eat chicken, mutton, fish. (Lacto-ova- vegetarian)','I eat milk, eggs and vegetables. I DO NOT eat chicken, mutton, fish. (Lacto-ova- vegetarian)'),
                ('I eat vegetables, milk, egg, chicken, mutton, fish. (Non vegetarian)','I eat vegetables, milk, egg, chicken, mutton, fish. (Non vegetarian)'),
                (' I eat vegetables, milk and fish. I DO NOT eat eggs, chicken and mutton. (Pescatarian)',' I eat vegetables, milk and fish. I DO NOT eat eggs, chicken and mutton. (Pescatarian)'),
]
glasseswater_c=[
            ('2-3 glasses','2-3 glasses'),
            ('4-5 glasses','4-5 glasses'),
            ('6-7 glasses','6-7 glasses'),
            ('8-9 glasses','8-9 glasses'),
            ('10 and more glasses','10 and more glasses'),
]
foodtime_c=[
            ('At school (during recess or available in school canteen','At school (during recess or available in school canteen)'),
            ('After school on my way home','After school on my way home'),
            ('In the evening as snacks','In the evening as snacks'),
            ('When I go out with my family members','When I go out with my family members'),
            ('When I go out to play with my friends','When I go out to play with my friends'),
]
middaymeal_c=[
            ('Yes, I get it and I love it','Yes, I get it and I love it'),
            ('Yes, I get it but I do not like it so I eat something else','Yes, I get it but I do not like it so I eat something else'),
            ('No, I do not get mid-day meal in my school','No, I do not get mid-day meal in my school'),
]
beforelock_c=[
        ('I carry my tiffin daily','I carry my tiffin daily'),
        ('I carry my tiffin only once a week I carry my tiffin 2-3 times a week','I carry my tiffin only once a week I carry my tiffin 2-3 times a week'),
        ('I carry my tiffin more than 3 times a week I never carry my tiffin','I carry my tiffin more than 3 times a week I never carry my tiffin'),
        ('I live in a hostel in the school','I live in a hostel in the school'),
]


class DailySchedule(forms.ModelForm):
    class Meta:
        model = DailyScheduleForm
        fields = ['sleepfrom','sleepto','eatfrom','eatto','studyfrom','studyto','playfrom','playto','housework','activities']

class BodyForm(forms.ModelForm):
    class Meta:
        model = BodyModel
        fields = ['weight','weightunit','height','heightunit','bmi','waist','waistunit','hip','hipunit','whratio']
 
class EatTodayForm(forms.ModelForm):
    class Meta:
        model = EatTodayModel
        fields = ['foodhabbits','foodallergies']


class DietForm(forms.ModelForm):
    class Meta:
        model = DietModel
        fields = ['mealtype','timefrom','timeto','rotiquantity','rotiunit','ricequantity','riceunit','pohaquantity','pohaunit','upmaquantity','upmaunit','teaquantity','teaunit','coffeequantity','coffeeunit','milkquantity','milkunit','vadaquantity','biscuitquantity','dalquantity','dalunit','gujratidalquantity','gujratidalunit','toordalquantity','toordalunit','moongdalquantity','moongdalunit','palakquantity','palakunit']

class studentprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = studentprof
        fields = ('uid','birthdate','age','schoolname','schoolcordinatorincharge','schooladdress','schoolcontactinformation','uploaded_photo',)
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class ngprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = ngprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class mentorprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = mentorprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class msprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = msprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class awprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = awprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }

class scprofForm(forms.ModelForm):
    birthdate=forms.DateField(input_formats='%Y/%m/%d',widget=forms.DateInput(attrs={'autocomplete':'off','class':'some_class','placeholder':'yyyy/mm/dd'}))
    
    class Meta:
        model = scprof
        fields = '__all__'
        widgets = {
                    'birthdate': DatePickerInput(format='%m/%d/%Y'), 
                 }
class FeedbackForm(forms.ModelForm):
    class Meta:
        model  = FeedbackModel 
        fields = ['name','issues','suggestions']
        widgets = {
            'issues': Textarea(attrs={'cols': 5, 'rows': 5}),
            'suggestions': Textarea(attrs={'cols': 5, 'rows': 5}),
        }
        
# class DietRecallForm(forms.ModelForm):
#     uid =forms.CharField( widget=forms.TextInput(attrs={'readonly':'readonly'}),initial='SMP'+''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5)))
#     eathabit = forms.ChoiceField(label='What is your dietary habit?',choices = eathabit_c)
#     glasseswater = forms.ChoiceField(label='How many glasses of water do you drink in a day?',choices = glasseswater_c)
#     foodtime = forms.MultipleChoiceField(label='When do you consume these foods? (Tick all that apply)',choices = foodtime_c)
#     beforelock = forms.ChoiceField(label='Before the lockdown, when you went to the school, how often did you carry Tiffin?',choices = beforelock_c)
#     middaymeal = forms.ChoiceField(label='Did you get a Mid-day meal in your school before the lockdown?',choices = middaymeal_c)
#     class Meta:
#         model=DietRecallModel
#         fields=['eathabit','glasseswater','foodtime','beforelock','middaymeal','uid']