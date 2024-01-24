from django.db import models


from django.conf import settings
# Create your models here.
def Path_Site_Logo(instance,filename):

    return "Cloud_Site/Site_Profile/%s/Site_Logo.jpeg"%(instance.Site_Name_en )

class Cloud_Site(models.Model):
    Site_Name_ar = models.CharField(blank=True,max_length=200 ,null=True , verbose_name='Site_Name_ar' , unique = True)
    Site_Name_en = models.CharField(blank=True,max_length=200 ,null=False , verbose_name='Site_Name_en' , unique = True)
    Site_Logo = models.ImageField(default='default.jpg', upload_to=Path_Site_Logo , blank=True , null=True)
    Super_User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL , null = True , blank= True, related_name='SuperUser')
    def __str__(self):
         return str(self.Site_Name_en)

    class Meta:
        db_table = 'Cloud_Site'

class DEPARTEMNTS(models.Model):
    Site = models.ForeignKey(Cloud_Site,  on_delete=models.SET_NULL , null = True )
    AR_Name = models.CharField( max_length=21,blank=True,null=True)
    EN_Name = models.CharField( max_length=21,blank=True,null=True)
    Manger = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL , null = True , blank= True, related_name='DepartementManger')

    def __str__(self):
        return '%s %s' % (self.Site.Site_Name_en, self.EN_Name)
    class Meta:
        db_table = 'DEPARTEMNTS_Site'
