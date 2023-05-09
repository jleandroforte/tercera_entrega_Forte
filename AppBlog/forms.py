
# En este archivo creamos los forms para las clases del modelo

from django import forms

from django import forms

class Formulario_Etiquetas(forms.Form): 
    etiquetas_del_post=forms.CharField(required=True,max_length=255)
    
    def __str__(self):
        return self.etiquetas_del_post()