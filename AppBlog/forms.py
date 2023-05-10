
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
