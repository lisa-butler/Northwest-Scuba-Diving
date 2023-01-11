from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('newsletter_signup_success/<email>', views.newsletter_signup_success, name='newsletter_signup_success'),
]
