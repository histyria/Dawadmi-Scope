from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse , HttpResponse
from .models import *
from .forms import LoginForm , UserRegistrationForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
def is_member(user, *group_names):
    if user.is_authenticated:
        if bool(user.groups.filter(name__in=group_names)):
            return True
    return False  


class SigninView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:index")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        just_logged_out = False
        try:
            if self.request.GET['ref'] == "logout":
                just_logged_out = True
        except:
            pass
        context['just_logged_out'] = just_logged_out
        if self.request.method == "GET":
            context['form'] = LoginForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        return super().post(request, *args, **kwargs)
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        DEPARTEMNT = request.POST.get('DEPARTEMNT')
        print(DEPARTEMNT)
        if form.is_valid():
            user = form.save()
        
            user.save()
            login(request, user)
            return redirect('home:index')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(request=request, template_name = "users/Sign_up.html", context={"form": form} )


def Get_Departement_list(request):
    if request.method == "GET":
        id_Hospital = request.GET.get('id_Hospital')
        data = DEPARTEMNTS.objects.filter(Dep_Site__id = id_Hospital ).values()
        return JsonResponse({'data': list(data)})

def Get_Departement(request):
    id_Hospital = request.GET.get('id_Site_id')
    print(id_Hospital)
    sid = Cloud_Site.objects.get(id = id_Hospital)
    get_dep = DEPARTEMNTS.objects.filter(Site = sid )
    print(get_dep)
    data = render_to_string('users/dep.html',{'data': get_dep},request=request)
    return JsonResponse(data , safe=False)