from django.db import models
from users.models import DEPARTEMNTS
# Create your models here.

from django.conf import settings

from django.urls import reverse
from .choices_models import *
from .Category_Event import *
class ovr_basemodel(models.Model):
    creator_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    creator_date = models.DateTimeField(auto_now=True)



class CONFIDENTIAL_OVR_QuerySet(models.QuerySet):
    def by_user_id(self, user_id):
        return self.filter(creator_by=user_id)

    def by_sec(self, sec_id):
        return self.filter(Assign_To_Section__Departemnt_Name__id=sec_id)


class CONFIDENTIAL_OVR_Manager(models.Manager):



    def by_user_id(self, user_id):
        return self.get_queryset().by_user_id(user_id)
    
    def by_sec(self, sec_id):
        return self.get_queryset().by_sec(sec_id)
    

    def get_queryset(self):
        return CONFIDENTIAL_OVR_QuerySet(self.model, using=self._db)

class CONFIDENTIAL_OVR_tickit(ovr_basemodel):


    Date_Time_of_Event = models.DateTimeField(auto_now=True , verbose_name ="Event Date & Time تاريخ الحادثة والوقت")
    Location = models.ForeignKey(DEPARTEMNTS, on_delete=models.CASCADE  , verbose_name ="Location | موقع الحادث",related_name='Location',null=True, blank=True)
    section_accident_occurred = models.ForeignKey(DEPARTEMNTS, on_delete=models.CASCADE  , verbose_name ="Reporting Department / Section | إدارة مرسل التقرير ",null=True, blank=True)
    Description = models.TextField( verbose_name ="Description | نبذة مختصرة")
    patient_type = models.CharField(max_length=100, choices=patient_type_list , default='Visitor زائر' , verbose_name =" patient type | تصنيف المريض ",null=True, blank=True)
    Event_type = models.CharField(max_length=200, choices=Event_type  , verbose_name ="Event type |نوع الحدث",null=True, blank=True)
    Injury_occurred = models.CharField(max_length=20, choices=Injury_occurred  , verbose_name ="Injury occurred? | هل من إصابات؟",null=True, blank=True)
    Level_of_Harm = models.ForeignKey(Level_of_Harm  , verbose_name ="Level of Harm |مستوى الضرر", related_name='LevelofHarm', on_delete=models.SET_NULL , null=True)
    Likelihood_Category = models.ForeignKey( Likelihood_Category , verbose_name ="Likelihood Category | فئة الإحتمالية", related_name='Likelihood_Category', null=True , on_delete=models.SET_NULL)
    Risk_Classification = models.CharField(max_length=20 , null=True, blank=True, verbose_name =" Risk Classification & Rating (Autofill) ")
    Event_Category = models.ManyToManyField(Event_Category,related_name='Events_Category' , verbose_name =" Event Category | فئة الحدث ", blank=True)
    Contributing_Factors  = models.ManyToManyField(Contributing_Factors, verbose_name =" Contributing Factors | عوامل مساهمة* ", blank=True)
    Assign_To_Section = models.ManyToManyField(Quality_Departement_Service,  verbose_name ="Assign To Department / Section | إسناد إلى إدارة / قسم", blank=True)
    Assign_dateTime = models.DateTimeField(null=True, blank=True)
    state = models.CharField(max_length=20, choices=States, default="Waiting for response")


    objects = CONFIDENTIAL_OVR_Manager()

    def get_absolute_url(self):
        return reverse("CONFIDENTIAL_OVR:view_ticket_ovr", kwargs={"ovr_id": self.id})
    def get_Assign_Section(self):
        return "\n".join([p.Assign_To_Section for p in self.Assign_To_Section.all()])
    def __str__(self):
        return str(self.section_accident_occurred)
    
    class Meta:
        verbose_name_plural = " OVR Tickit List "   


class Replay_Ovr(models.Model):
    OVR_ID = models.ForeignKey(CONFIDENTIAL_OVR_tickit, on_delete=models.CASCADE)
    comment = models.TextField(blank=False, default="")
    Replay_User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True , verbose_name='Replay_User')
    dateTime = models.DateTimeField(auto_now=True)
    Privet = models.BooleanField(default=False)

    class Meta:
        db_table = 'Replay_Ovr'