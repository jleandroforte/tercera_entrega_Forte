from django.db import models
from datetime import *

# Create your models here.

class Posts(models.Model): 
    titulo=models.CharField(max_length=255) 
    cuerpo=models.TextField() 
    fecha_publicacion=models.DateField()
    autor=models.CharField(max_length=255)
    email_autor=models.EmailField()

class Autor(models.Model): 
    nombre_autor=models.CharField(max_length=255)
    
    def _str_(self):
        return self.nombre_autor()
        
class Etiquetas(models.Model): 
    etiquetas_del_post = models.CharField(max_length=255)

    def _str_(self):
        return self.etiquetas_del_post
