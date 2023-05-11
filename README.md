# tercera_entrega_Forte
Proyecto Tercera Entrega del Curso Python Comision 40440
El proyecto está armando en Django 4.2. 
El acceso básico es a “http://127.0.0.1:8000/AppBlog/”  O al puerto que se indique, pero es indispensable ir a /AppBlog para empezar. 

El sitio se compone de una aplicación (‘AppBlog’) con  4 modelos/urls: 
AppBlog/: Esta la página de Inicio, donde buscamos si una etiqueta se encuentra en la base de datos. 
AppBlog/autores/: Donde se envían a la base de datos la información de los autores de un post (nombre del autor) 
AppBlog/etiquetas/: Donde se envían a la base de datos las etiquetas de los posts.Estas estiquetas despues pueden ser buscadas desde el inicio.
AppBlog/posts/: Donde se envían a la base de datos las siguientes variables relacionadas a posteos con los siguientes parámetros: 

titulo=models.CharField(max_length=255) 
cuerpo=models.TextField() 
fecha_publicacion=models.DateField()
autor=models.CharField(max_length=255)
email_autor=models.EmailField()

Para chequear que lo que enviamos por formulario esté en la base de datos más allá de la barra de búsqueda en Inicio (sólo para etiquetas) debemos ir al admin: http://127.0.0.1:8000/admin/ 

Finalmente, el proyecto tiene herencia de templates, podemos navegar entre categorías en la parte superior de cada página. 

El proyecto ya cuenta con 2 etiquetas en la base de datos ‘Economía’ e ‘Historia’, un usuario puede buscarlas en la página de inicio - AppBlog/, y va a ver un mensaje indicando que se encuentra en la base. Alternativamente, si se busca otra etiqueta (o cualquier otro string realmente) sin agregarla previamente a la base de datos desde AppBlog/etiquetas/ va a recibir un mensaje indicando que la etiqueta no se encuentra en la base de datos. 	 

Internamente, la estructura de archivos es bastante simple, tenemos una sola App, llamada AppBlog, y dentro de ella se pueden encontrar los modelos (models.py), las urls (se debe revisar el archivo urls.py dentro de la App, el urls.py de la carpeta 'blog' solo conecta con las urls de la App), los templates, incluyendo el Base del que todos los demás heredan la barra de navegación, las views.py y los forms con la funcionalidad de los formularios en forms.py. Para cuestiones visuales usé bootstrap, los archivos de bootstrap están en la carpeta static. 
