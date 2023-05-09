
from django.urls import path, include
from AppBlog import views


urlpatterns = [
   path('',views.inicio, name='Inicio'),
   path('autores/',views.autores, name='Autores'),  
   path('etiquetas/',views.etiquetas, name='Etiquetas'),
   path('posts/',views.posts, name='Posts'),  
   path('crear_etiquetas/',views.crear_etiquetas, name='crear_etiquetas'),

  


]