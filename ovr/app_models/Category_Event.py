from django.db import models
from users.models import DEPARTEMNTS
# Create your models here.

from django.conf import settings

from django.urls import reverse
from .choices_models import *




    

        

class Contributing_Factors(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contributing Factors | عوامل مساهمة"  
        db_table = 'Contributing_Factors' 

#Level of Harm |مستوى الضرر
class Level_of_Harm(models.Model):
    name = models.CharField(max_length=20)
    risk_value = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Level of Harm |مستوى الضرر"  
        db_table = 'Level_of_Harm' 


#Likelihood Category | فئة الإحتمالية
class Likelihood_Category(models.Model):
    name = models.CharField(max_length=20)
    risk_value = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Likelihood Category | فئة الإحتمالية"
        db_table = 'Likelihood_Category' 



# الأقسم المشموله بخدمات الجودة
class Quality_Departement_Service(models.Model):
    Departemnt_Name = models.ForeignKey(DEPARTEMNTS, on_delete=models.CASCADE   , verbose_name =" Departemnt Name | إسم القسم",null=True, blank=True)
    Users_Access = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name =" Users_Access  | الأعضاء المسؤولين ", blank=True)
    def __str__(self):
        return str(self.Departemnt_Name)
    class Meta:
        verbose_name_plural = "Quality Departement Service "  
        db_table = 'Quality_Departement_Service' 

# فئة الحدث
class Event_Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Event Category | فئة الحدث "  
        db_table = 'Event_Category' 



