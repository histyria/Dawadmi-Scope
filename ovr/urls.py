from django.urls import path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 
app_name = 'ovr'

urlpatterns = [
    path('1/', index, name="index"),
    path('Get_By_Section/', Get_By_Section, name="Get_By_Section"),
    path('Quality_OVR_list/', Quality_OVR_list, name="Quality_OVR_list"),
    path('Assign_To_Sec/<int:ovr_id>', PostUpdateView.as_view(), name="Assign_To_Sec"),

    path('OVR/create/', OVR_create_view.as_view(), name='OVR_create_view'),
    path('Hospital/Policy_List', Departement_Policy_View, name='Policy_List'),
    path('view_ticket_ovr/<int:ovr_id>', view_ticket_ovr, name="view_ticket_ovr"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

