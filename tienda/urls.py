from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Para redirigir la raíz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),  # Incluye las rutas de usuarios con namespace
    path('', RedirectView.as_view(url='/usuarios/registro/', permanent=False)),  # Redirige la raíz al registro
]
