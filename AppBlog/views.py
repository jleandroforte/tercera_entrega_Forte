
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

# funcion para crear etiquetas.     

def crear_etiquetas(request):   
   if request.method == "POST":
       formulario = Formulario_Etiquetas(request.POST)

       if formulario.is_valid():
           etiquetas_del_post = formulario.cleaned_data["etiquetas_del_post"]
           etiquetas = Etiquetas(etiquetas_del_post=etiquetas_del_post)
           etiquetas.save()
        
           url_exitosa = reverse('crear_etiquetas')  
           return redirect(url_exitosa)
       
   else:  
       formulario = Formulario_Etiquetas()
   
   http_response = render(
       request=request,
       template_name='AppBlog/formulario_etiquetas.html',
       context={'formulario': formulario}
   )
   return http_response

# funcion para buscar etiquetas 

def buscar_etiquetas(request):
    nombre_de_busqueda = request.GET.get('etiquetas_del_post')
    print(nombre_de_busqueda)

    if nombre_de_busqueda:
        
        lista = Etiquetas.objects.filter(etiquetas_del_post__icontains=nombre_de_busqueda)
        
        if len(lista) != 0:
           
            form = Formulario_Etiquetas()
            contexto = {
                'etiquetas_del_post': lista,  
                'form': form  
            }
            return render(request, 'AppBlog/buscar_etiquetas.html', context=contexto)
        else:
            mensaje = "No se encontraron etiquetas con ese nombre."
            return render(request, 'AppBlog/buscar_etiquetas.html', {"mensaje": mensaje, "form": Formulario_Etiquetas()})
    else:
        
        return render(request, 'AppBlog/buscar_etiquetas.html', {"form": Formulario_Etiquetas()})



def crear_autor(request):   
   if request.method == "POST":
       formulario = Formulario_Autor(request.POST)

       if formulario.is_valid():
           nombre_autor = formulario.cleaned_data["nombre_autor"]
           autores = Autor(nombre_autor=nombre_autor)
           autores.save()
        
           url_exitosa = reverse('crear_autor')  
           return redirect(url_exitosa)
       
   else:  
       formulario = Formulario_Autor()
   
   http_response = render(
       request=request,
       template_name='AppBlog/formulario_autor.html',
       context={'formulario': formulario}
   )
   return http_response