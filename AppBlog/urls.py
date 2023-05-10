
from django.urls import path, include
from AppBlog import views


urlpatterns = [
   path('',views.buscar_etiquetas, name='Inicio'),
   path('autores/',views.autores, name='Autores'),  
   path('etiquetas/',views.crear_etiquetas, name='Etiquetas'),
   path('posts/',views.posts, name='Posts'),  
   path('crear_etiquetas/',views.crear_etiquetas, name='crear_etiquetas'),
   path('buscar_etiquetas/',views.buscar_etiquetas, name='buscar_etiquetas'),
   path('crear_autor/',views.crear_autor, name='crear_autor'),  

]