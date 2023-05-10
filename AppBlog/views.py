
from django.shortcuts import render, redirect
from django.urls import reverse


from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

from AppBlog.models import *
from AppBlog.forms import *
from django.urls import reverse
from django.shortcuts import redirect
from .models import *

# Create your views here.


def inicio(request): 
    return render(request, 'inicio.html')


def posts(request): 
    return render(request, 'AppBlog/posts.html')

def autores(request): 
    return render(request, 'AppBlog/autores.html')


def etiquetas(request): 
    return render(request, 'AppBlog/etiquetas.html')


def crear_etiquetas(request):
    if request.method == "POST":
        formulario = Formulario_Etiquetas(request.POST)

        if formulario.is_valid():
            etiqueta = formulario.save()

            # Redirecciono al usuario a la lista de etiquetas
            url_exitosa = reverse('crear_etiquetas')  
            return redirect(url_exitosa)

    else:
        formulario = Formulario_Etiquetas()

    return render(request, 'AppBlog/crear_etiquetas.html', {'formulario': formulario})


