from django.shortcuts import render , get_object_or_404
from .models import *
# Create your views here.

def index(request ):
    return render(request, 'home/index.html' )


def login_view(request ):
    return render(request, 'users/login.html' )


def Sign_up_view(request ):
    return render(request, 'users/Sign_up.html' )

