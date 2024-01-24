from django.db import models
from datetime import datetime
# Create your models here.
from users.models import User
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

from .validators import *

def Patient_Files_ID_Images(instance,filename):
    today = instance.en_patiant_name + '-' + instance.ar_patiant_name

    return "Medecal_Record/Archive_Patient_Files/%s/%s.jpeg"%(instance.patiant_no ,today)




# جدول الجنسيات
class Nationality(models.Model):  
    country_code = models.CharField(max_length=3, blank=True, null=True)  # Field name made lowercase.
    country_desc = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    area_code = models.CharField(max_length=2, blank=True, null=True)  # Field name made lowercase.
    male_nationality_desc = models.CharField(max_length=16, blank=True, null=True)  # Field name made lowercase.
    female_nationality_desc = models.CharField(max_length=16, blank=True, null=True)  # Field name made lowercase.
    country_e_desc = models.CharField(max_length=23, blank=True, null=True)  # Field name made lowercase.
    nationality_e_desc = models.CharField(max_length=15, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
         return str(self.country_desc) + '  - ' + str(self.nationality_e_desc)

    class Meta:
        db_table = 'Nationality'
gender = (
        ('1','Male'),
        ('2','Female')
      
    )


# جدول معلومات المريض
class Patiant_File_NO(models.Model):
   
    registration_date = models.DateField(auto_now_add=True)  
    patiant_no = models.IntegerField()  
    ar_patiant_name = models.CharField(max_length=200 , blank=True, null=True)  
    en_patiant_name = models.CharField(max_length=200 , blank=True, null=True)  
    birth_date = models.DateField(blank=False, null=False)  
    gender =  models.CharField(max_length=200, null=True,choices=gender)
    nationalty = models.ForeignKey(Nationality, on_delete=models.DO_NOTHING, blank=True, null=True )
    social_number = models.CharField( max_length=200 , blank=True, null=True , unique=False )  
    address = models.CharField(max_length=200,blank=True, null=True)  
    mobile_no = models.IntegerField(blank=True, null=False , unique=False)  
    mother_name = models.CharField(max_length=200,blank=True, null=True)  
    mother_med_no = models.IntegerField(blank=True, null=True)  
    patiant_no_form = models.CharField(max_length=200,blank=True, null=True)  
    smok_status = models.CharField(max_length=200,blank=True, null=True)  
    ins_user_code = models.ForeignKey(User, on_delete=models.DO_NOTHING,  related_name='Patiant_File_NO_insert_user_code' ,null=True, blank=True)
    ins_user_date = models.DateField(auto_now_add=True ,blank=True, null=True)  
    upd_user_code = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    upd_user_date = models.DateField( blank=True, null=True)  
    mother_id = models.IntegerField(blank=True, null=True)
    ID_image = models.ImageField(upload_to=Patient_Files_ID_Images , blank=True, null=True)
    class Meta:
        db_table = 'PatiantS_File_NO'
    def __str__(self):
         return str(self.patiant_no)
    def save(self, *args, **kwargs):
        date_id = self.registration_date
        if date_id == None :
            self.registration_date = datetime.now() 
            return super().save(*args, **kwargs)


import datetime as dt
class Patiant_Or_Appointment(models.Model):
    Patiant_No = models.ForeignKey(Patiant_File_NO , on_delete=models.CASCADE , related_name='Appointment_Patient')
    Patiant_Phone = PhoneNumberField(help_text= 'EXP : 966563481855')
    Date = models.DateField(validators=[validate_day])
    time = models.TimeField()
    begin_time = models.TimeField(default=dt.time(00, 00))
    
    def __str__(self):
         return str(self.id) 
    def save(self, *args, **kwargs):
        name = self.Patiant_No.ar_patiant_name
        number = self.Patiant_Phone
        day = self.Date.day
        date = self.Date()
        time = self.begin_time
        print(name)
        print(number)
        print(day)
        print(date)
        print(time)
        return super().save(*args, **kwargs)
    class Meta:
        db_table = 'Patiant_Or_AppointmentS'
