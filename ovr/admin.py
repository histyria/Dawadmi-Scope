from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Contributing_Factors)
admin.site.register(Likelihood_Category)
admin.site.register(Level_of_Harm)
admin.site.register(Event_Category)
admin.site.register(Quality_Departement_Service)
from cbahi.models import *
admin.site.register(Replay_Ovr)

class Departement_Policy_modelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'Site_Name'  ,  'Departemnt_Name'  , 'Policy_Titel_AR' ,'Policy_Titel_EN'   , 'add_date'   ]

admin.site.register(Departement_Policy_model, Departement_Policy_modelAdmin)

from users.models import User

from django.contrib.contenttypes.models import ContentType
class CONFIDENTIAL_OVR_tickitAdmin(admin.ModelAdmin):
    list_display = ['id','Location' , 'patient_type','Event_type', 'Level_of_Harm','Likelihood_Category' ,  'Risk_Classification'  ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # for s in qs:
        if request.user.is_superuser:
            return qs
        return qs.filter(creator_by__role__name = 'Quality_Team')
   
    #readonly_fields=('creator_by' , 'Location','section_accident_occurred' ,'Description' ,'Event_Category', 'patient_type' ,'Event_type','state',  'Contributing_Factors','Injury_occurred' , 'Level_of_Harm','Likelihood_Category' ,  'Risk_Classification' )
admin.site.register(CONFIDENTIAL_OVR_tickit, CONFIDENTIAL_OVR_tickitAdmin)



