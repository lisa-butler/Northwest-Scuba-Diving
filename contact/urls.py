from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_request_success', views.contact_request_success, name='contact_request_success'),
]
