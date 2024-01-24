from django.contrib import admin
from django.forms import widgets

# Register your models here.
from .models import *
from .forms import *


class Patiant_File_NOAdmin(admin.ModelAdmin):
    
    
    list_display = ['patiant_no' , 'ar_patiant_name', 'en_patiant_name' , 'gender'  , 'birth_date' , 'nationalty']

admin.site.register(Patiant_File_NO, Patiant_File_NOAdmin)




class Patiant_Or_AppointmentAdmin(admin.ModelAdmin):
    form = Patiant_Or_AppointmentForm
admin.site.register(Patiant_Or_Appointment , Patiant_Or_AppointmentAdmin)

from django.contrib import admin
from .models import *
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.ModelForm):
    phone = PhoneNumberField(region="US")
    class Meta:
        fields = '__all__'
