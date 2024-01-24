from django.urls import path
from .views import *


app_name = 'home'
urlpatterns = [
    path('', index, name="index"),
    path('login/', login_view, name="login"),
    path('Sign_up/', Sign_up_view, name="Sign_up"),
 
 
 
]