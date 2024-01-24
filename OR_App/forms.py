
from django import forms
from django.forms import ModelForm
from .models import *




import datetime as dt
HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]

class Patiant_Or_AppointmentForm(forms.ModelForm):
    class Meta:
        model = Patiant_Or_Appointment
        fields = '__all__'
        widgets = {'begin_time': forms.Select(choices=HOUR_CHOICES)}
        
        
        
