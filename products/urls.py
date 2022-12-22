from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('courses/', views.courses, name='courses'),
    path('qualified/', views.qualified, name='qualified'),
    path('gear/', views.gear, name='gear'),
    path('add/', views.add_product, name='add_product'),
]
