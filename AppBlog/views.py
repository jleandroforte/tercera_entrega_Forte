
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


def crear_etiquetas(request):   # funcion para crear etiquetas.     
   if request.method == "POST":
       formulario = Formulario_Etiquetas(request.POST)

       if formulario.is_valid():
           etiquetas_del_post = formulario.cleaned_data["etiquetas_del_post"]
           etiquetas = Etiquetas(etiquetas_del_post=etiquetas_del_post)
           etiquetas.save()
           
           # Redirecciono al usuario a la lista de cursos
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
    # Obtener el valor del parámetro 'etiquetas_del_post' desde la URL
    nombre_de_busqueda = request.GET.get('etiquetas_del_post')
    print(nombre_de_busqueda)

    if nombre_de_busqueda:
        # Si se proporciona un valor de búsqueda
        # Filtrar las etiquetas que contengan el valor de búsqueda
        lista = Etiquetas.objects.filter(etiquetas_del_post__icontains=nombre_de_busqueda)
        
        if len(lista) != 0:
            # Si se encontraron etiquetas que coinciden con la búsqueda
            # Crear una instancia del formulario para mostrarlo en la plantilla
            form = Formulario_Etiquetas()
            contexto = {
                'etiquetas_del_post': lista,  # Pasar las etiquetas encontradas al contexto
                'form': form  # Pasar el formulario al contexto
            }
            return render(request, 'AppBlog/buscar_etiquetas.html', context=contexto)
        else:
            # Si no se encontraron etiquetas que coincidan con la búsqueda
            mensaje = "No se encontraron etiquetas con ese nombre."
            return render(request, 'AppBlog/buscar_etiquetas.html', {"mensaje": mensaje, "form": Formulario_Etiquetas()})
    else:
        # Si no se proporcionó ningún dato de búsqueda
        # Mostrar solo el formulario vacío en la plantilla
        return render(request, 'AppBlog/buscar_etiquetas.html', {"form": Formulario_Etiquetas()})
