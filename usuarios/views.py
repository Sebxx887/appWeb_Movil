from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
import qrcode
from io import BytesIO
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('registro')  # Redirige al registro después del login
    else:
        form = AuthenticationForm()
    return render(request, 'registro.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('productos:lista_zapatillas')  # Redirigir al usuario a la página de productos después de registrarse
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form_registro': form})

def generar_qr(request):
    # Enlace de descarga de la app
    link_descarga = "https://www.mediafire.com/file/ot1s7hptqdoutpd/app-debug.apk/file"

    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link_descarga)
    qr.make(fit=True)

    # Generar la imagen QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen QR en memoria
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Retornar la imagen como respuesta
    return HttpResponse(buffer, content_type="image/png")