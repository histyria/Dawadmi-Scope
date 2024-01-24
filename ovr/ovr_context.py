from .models import *
from users.models import *
from .forms import *
def User_Departement_Manager( user_id):
        return User.objects.filter(id=user_id , role__name = 'Departement_Manager' ).exists()




def User_Quality_Team( user_id):
        return User.objects.filter(id=user_id , site_role__name = 'Quality_Team' ).exists()



def User_Departement_Access( user_id):
        return Quality_Departement_Service.objects.filter(Users_Access__id = user_id).exists()





def user_list (request):
    if request.user.is_authenticated :
       # sec_id = request.user.DEPARTEMNT.id
        #print(sec_id)
        By_usr = CONFIDENTIAL_OVR_tickit.objects.by_user_id(request.user)
        #is_Manager = User_Departement_Manager(request.user.id)
        Departement_Access = User_Departement_Access(request.user.id)
        ovr_list =  CONFIDENTIAL_OVR_tickit.objects.all()
        
        Quality_Access = User_Quality_Team(request.user.id)
        #by_sec = CONFIDENTIAL_OVR_tickit.objects.by_sec(sec_id)
        form = CONFIDENTIAL_OVR_tickitForm
        CommentForm = Replay_OvrForm
        Assign_To_Section = Assign_To_SectionForm

        context = {
              'ovr_list':ovr_list ,
             #'is_Manager':is_Manager ,
             'Departement_Access':Departement_Access ,
             'Quality_Access':Quality_Access ,
        'By_usr':By_usr ,
           # 'by_sec':by_sec , 
            'form':form , 
            'CommentForm':CommentForm , 
            'Assign_To_SectionForm' :Assign_To_SectionForm
            }
        return context
    else :
        context = {
        'By_usr':'' ,
            'by_sec':'' , 
            
            }
        return context