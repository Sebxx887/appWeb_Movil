from django.urls import path
from . import views

app_name = 'usuarios'  # Declara el namespace 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
]
