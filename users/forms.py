from django import forms
from django.forms import ModelForm
from home.models import *
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'remember_me')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model =  User
        fields = ['first_name', 'last_name', 'username' , 'Site_id' , 'DEPARTEMNT', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['DEPARTEMNT'].widget.attrs['name'] = "DEPARTEMNT-dev"
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['DEPARTEMNT'].queryset = DEPARTEMNTS.objects.none()
        
        if 'DEPARTEMNT' in self.data:
            self.fields['DEPARTEMNT'].queryset = DEPARTEMNTS.objects.all()
        elif self.instance.pk:
            self.fields['DEPARTEMNT'].queryset = DEPARTEMNTS.objects.all().filter(pk=self.instance.DEPARTEMNT.pk)
    
    def clean_user_name(self):
        Username = self.cleaned_data['Username'].lower()
        r = User.objects.filter(Username=Username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return Username
    

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email



class Support_TeamForm(forms.ModelForm):


    
    class Meta:
        model= Section_Support_Team
        fields=('__all__')
