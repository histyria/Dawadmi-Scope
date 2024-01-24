
from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.staticfiles import *
from django.conf import settings

from home.models import *

from .managers import  *
class User_Role(models.Model):
    
    name = models.CharField(max_length=200 , blank=True , null=True)

    def __str__(self):
         return str(self.name)
class User(AbstractUser):
   
   
    role = models.ForeignKey( User_Role, blank=True, null=True , on_delete=models.SET_NULL,)
    Site_id = models.ForeignKey( Cloud_Site, blank=True, null=True , on_delete=models.SET_NULL,)
    DEPARTEMNT = models.ForeignKey( DEPARTEMNTS, blank=True, null=True , on_delete=models.SET_NULL, related_name='user_departement')
   





def Path_Profile_Avatar(instance,filename):
    

    return "Cloud_Site/%s/Users/avataer/%s/avatar.jpeg"%(instance.user.id ,instance.user.username)

         
         
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='profile')
    bio = models.CharField(max_length=50, blank=True)
    avatar = models.FileField(upload_to=Path_Profile_Avatar)
    
    def __str__(self):
       fir = str(self.user)
       if not self.user.first_name   :
           return fir
       else :
        return '%s %s' % (self.user.first_name, self.user.last_name)
    
  

# Section_Name = models.ForeignKey( DEPARTEMNTS, on_delete=models.SET_NULL, related_name='issu_departement', limit_choices_to={'Ticket_Service' : True })

class Services(models.Model):
    Section_Name = models.ForeignKey( DEPARTEMNTS, null=True ,on_delete=models.SET_NULL, related_name='Service_Section')
    Titel = models.CharField( max_length=21,)
    
    def __str__(self):
        return  self.Titel
    class Meta:
        db_table = 'Services'





from .managers import Support_TeamManager


class Section_Support_Team(models.Model):
    Section_Name = models.ForeignKey( DEPARTEMNTS, null=True ,on_delete=models.SET_NULL, related_name='Team_Section')
    Team_Name = models.CharField( max_length=21)
    Support_User = models.ManyToManyField(User, related_name='Support_User')
    Access_Services = models.ManyToManyField(Services, related_name='Services_list')
    team_query = Support_TeamManager()
    objects = models.Manager()
    def __str__(self):
        return  str(self.Team_Name)
    class Meta:
        db_table = 'Section_Support_Team'


