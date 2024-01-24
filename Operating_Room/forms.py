
from django import forms
from django.forms import ModelForm
from .models import *
from phonenumber_field.widgets import PhoneNumberPrefixWidget     
from django import forms
from phonenumber_field.formfields import PhoneNumberField




import datetime as dt
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]

class Patiant_Or_AppointmentForm(forms.ModelForm):
    Patiant_Phone = PhoneNumberField()
    Patiant_Phone.error_messages['invalid'] = 'خطأ في الرقم يجب أن يبدأ 966'
    class Meta:
        model = Patiant_Or_Appointment
        fields = '__all__'
        widgets = {'begin_time': forms.Select(choices=HOUR_CHOICES)}
        
     