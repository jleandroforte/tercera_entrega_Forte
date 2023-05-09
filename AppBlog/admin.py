from django.contrib import admin

# Register your models here.

from .models import Autor, Etiquetas,Posts 

admin.site.register(Autor)
admin.site.register(Etiquetas)
admin.site.register(Posts)
