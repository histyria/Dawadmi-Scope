from django.contrib import admin
from django.urls import include, path
from . import views
from . import views
import home.views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    
    
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/',views.SigninView.as_view(),name='login'),
    path("register/", views.register, name="user_register"),
    #path('accounts/', include('django.contrib.auth.urls')),
    path("Get_Departement/", views.Get_Departement, name="Get_Departement"),
]