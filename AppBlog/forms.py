
# En este archivo creamos los forms para las clases del modelo

from django import forms
from AppBlog.models import *

'''class Formulario_Etiquetas(forms.Form): 
    etiquetas_del_post=forms.CharField(required=True,max_length=255)
    
    def __str__(self):
        return self.etiquetas_del_post()'''
        
class Formulario_Etiquetas(forms.Form): 
    etiquetas_del_post = forms.CharField(required=True, max_length=255)

    def save(self):
        etiqueta = Etiquetas(etiquetas_del_post=self.cleaned_data['etiquetas_del_post'])
        etiqueta.save()
        return etiqueta


class Formulario_Autor(forms.Form): 
    nombre_autor = forms.CharField(required=True, max_length=255)

    def save(self):
        autor = Etiquetas(nombre_autor=self.cleaned_data['etiquetas_del_post'])
        autor.save()
        return autor

class Formulario_Posts(forms.Form): 
    titulo=forms.CharField(max_length=255) 
    cuerpo=forms.CharField(max_length=40000) 
    fecha_publicacion=forms.DateField()
    autor=forms.CharField(max_length=255)
    email_autor=forms.EmailField()
    
    def save(self):
        titulo = Posts(titulo=self.cleaned_data['titulo'])
        titulo.save()
        return titulo
   
    def save(self):
        cuerpo = Posts(cuerpo=self.cleaned_data['cuerpo'])
        cuerpo.save()
        return cuerpo
    
    def save(self):
        fecha_publicacion = Posts(fecha_publicacion=self.cleaned_data['fecha_publicacion'])
        fecha_publicacion.save()
        return fecha_publicacion
    
    def save(self):
        autor = Posts(autor=self.cleaned_data['autor'])
        autor.save()
        return autor
    
    def save(self):
        email_autor = Posts(email_autor=self.cleaned_data['autor'])
        email_autor.save()
        return email_autor