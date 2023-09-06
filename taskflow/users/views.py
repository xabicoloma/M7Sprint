from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import forms

# Create your views here.
@login_required
def logout(request):
    logout(request)


def registro(request):
    if request.method == "POST":
        formulario_p = forms.RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            username = formulario_p.cleaned_data["username"]
            print(username)
            messages.success(request, f'Cuenta creada de forma exitosa para el usuario {username}')
            user = formulario_p.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Hubo un error en el registro")
    formulario = forms.RegistroUsuarioForm()
    return render(request, 'register.html', {'formulario': formulario})