from django.contrib import admin
from django.urls import path, include
from usuarios import views as user_views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView  # Importa esta clase para redirigir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', user_views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/registro.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', RedirectView.as_view(url='/registro/', permanent=False)),  # Redirige la raíz al registro
] 
