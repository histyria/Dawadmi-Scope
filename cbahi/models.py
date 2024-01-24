from django.db import models

# Create your models here.
from home.models import *
def Path_Policy_File(instance,filename):
    
    return "media/cbahi/Policy/%s/%s/%s"%(instance.Site_Name , instance.Policy_Titel_EN, instance.Site_Name)


class Departement_Policy_model(models.Model):
    Site_Name = models.ForeignKey(Cloud_Site, on_delete=models.CASCADE   , verbose_name =" Hospital Name | إسم المستشفى",null=True, blank=True)
    Departemnt_Name = models.ForeignKey(DEPARTEMNTS, on_delete=models.CASCADE   , verbose_name =" Departemnt Name | إسم القسم",null=True, blank=True)
    Policy_Titel_AR = models.CharField(blank=True,max_length=200 ,null=True)
    Policy_Titel_EN = models.CharField(blank=True,max_length=200 ,null=True)
    Policy_description = models.TextField()
    Policy_File=models.FileField(upload_to=Path_Policy_File)
    add_date = models.DateTimeField( auto_now_add=True)
    Last_Update = models.DateTimeField( auto_now_add=False , blank=True , null=True) 
    class Meta:
        verbose_name_plural = "Departement_Policy | سياسات الأقسام "
        db_table = 'Quality_Departement_Policy' 

    def __str__(self):
        return str(self.Policy_Titel_AR)