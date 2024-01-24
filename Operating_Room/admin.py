from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.forms import widgets

# Register your models here.
from .models import *
from .forms import *


class Patiant_File_NOAdmin(admin.ModelAdmin):
    
    
    list_display = ['patiant_no' , 'ar_patiant_name', 'en_patiant_name' , 'gender'  , 'birth_date' , 'nationalty']

admin.site.register(Patiant_File_NO, Patiant_File_NOAdmin)
admin.site.register(Operation_type)




class Patiant_Or_AppointmentAdmin(admin.ModelAdmin):
    form = Patiant_Or_AppointmentForm
    list_display = ['Operation_Name' , 'Patiant_No' , 'Patiant_Phone', 'Date' , 'time'  , 'begin_time' ]
admin.site.register(Patiant_Or_Appointment , Patiant_Or_AppointmentAdmin)
