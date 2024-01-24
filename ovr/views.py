from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse

from django.template.loader import get_template
# Create your views here.
from django.shortcuts import render
from .forms import *
from django.views.generic import UpdateView, ListView


from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
# Create your views here.

from django.contrib.auth.decorators import login_required
from cbahi.models import *

def index(request):   
    ovr_list =  CONFIDENTIAL_OVR_tickit.objects.all()
    return render(request, 'ovr/index.html' ,{'ovr_list':ovr_list} )

def Get_By_Section(request):   

    return render(request, 'ovr/section_list.html'  )



def Quality_OVR_list(request):   

    return render(request, 'ovr/ovr-team.html'  )






from django.contrib.auth.decorators import login_required
def ovr_list(request):   
    listed = CONFIDENTIAL_OVR_tickit.objects.all()
    print(listed)
    return render(request, 'ovr/ovr_list.html' ,{'listed':listed} )

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
class OVR_create_view( CreateView):
    model = CONFIDENTIAL_OVR_tickit
    form_class = CONFIDENTIAL_OVR_tickitForm
    template_name = 'ovr/add_ovr.html'
    success_url = reverse_lazy('ovr:ovr_list')
    def form_valid(self, form):
        ovr = form.save(commit=False)
        ovr.creator_by = self.request.user
        ovr.section_accident_occurred = self.request.user.DEPARTEMNT
        ovr.save()
        return redirect('ovr:index')


def view_ticket_ovr(request, ovr_id):
    ticket = get_object_or_404(CONFIDENTIAL_OVR_tickit, id=ovr_id)
    form = Replay_OvrForm(request.POST,request.FILES)
    replay_count = Replay_Ovr.objects.filter(OVR_ID = ticket ).count()
    if form.is_valid():
        Replay = form.save(commit=False)
        Replay.OVR_ID = ticket
        Replay.Replay_User = request.user
        Replay.save()
        ticket.state = 'Answered'
        ticket.save()
        return redirect('ovr:view_ticket_ovr' , ovr_id = ticket.id)
    rep = Replay_Ovr.objects.filter(OVR_ID = ticket )
    return render(request, 'ovr\ovr_ticket_detail.html' ,{   'replay_count':replay_count , 'listed':ticket , 'rep':rep} )
   


from django.utils import timezone





class PostUpdateView(UpdateView):
    model = CONFIDENTIAL_OVR_tickit
    fields = ('Assign_To_Section',)
    template_name = 'edit_post.html'
    pk_url_kwarg = 'ovr_id'
    context_object_name = 'ticket'

    def form_valid(self, form):
        post = form.save(commit=False)
        
        post.Assign_dateTime = timezone.now()
        post.state = 'Assigned'
        post.save()
        return redirect('home:index')
    



def Assign_To_Sec(request, ovr_id):
    ticket = get_object_or_404(CONFIDENTIAL_OVR_tickit, id=ovr_id)
    
    replay_count = Replay_Ovr.objects.filter(OVR_ID = ticket ).count()
    form = CONFIDENTIAL_OVR_tickitForm(request.POST,request.FILES)
    if form.is_valid():
        
        Assign_To_Section = request.POST.get('Assign_To_Section')
        Replay = form.save(commit=False)
        Replay.Assign_dateTime = timezone.now()
        Replay.Assign_To_Section = Assign_To_Section
        Replay.save()

        ticket.Assign_To_Section = Assign_To_Section
        ticket.state = 'Assigned'
        ticket.save()
        return redirect('ovr:view_ticket_ovr' , ovr_id = ticket.id)
    rep = Replay_Ovr.objects.filter(OVR_ID = ticket )
    return render(request, 'ovr\ovr_ticket_detail.html' ,{   'replay_count':replay_count , 'listed':ticket , 'rep':rep} )
   



def Departement_Policy_View(request):   
    policy = Departement_Policy_model.objects.all()

    return render(request, 'ovr/policy_list.html' , {'policy':policy}  )

