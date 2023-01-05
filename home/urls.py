from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('get_in_contact', views.get_in_contact, name='get_in_contact'),
    path('message_sent', views.message_sent, name='message_sent'),
]
