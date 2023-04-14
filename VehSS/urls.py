from django.contrib import admin
from django.urls import path
from VehSS import views

urlpatterns = [
    path("",views.index1,name='home'),
    path("about",views.about,name='about'),
    path("home",views.home,name='home'),
    path("services",views.services,name='services'),
    path("register",views.registerPage,name='register'),
    path("gotit",views.gotit,name='gotit'),
    path("add_vehicle",views.add_vehicle,name='add_vehicle'),
    path("summary",views.summary,name='summary'),
    path("minusvehicle",views.summary,name='summary'),
    path("contact",views.contact,name='contact'),
    path("form",views.formu,name='form'),
    path("index1",views.index1,name='index1'),
    path("userview",views.userview,name='userview'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout'),
    path("owner",views.owner,name='owner'),
    path("traveller",views.traveller,name='traveller'),
    path("traveller_a",views.traveller_a,name='traveller_a'),
    path("traveller_v",views.traveller_v,name='traveller_v'),
    path("traveller_n",views.traveller_n,name='traveller_n'),





    
]