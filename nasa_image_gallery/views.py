# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')

# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request,x):

    images=services_nasa_image_gallery.getAllImages(input=None)  ##Importamos imágenes de "services_nasa_image_gallery"
    
    favourite_list=services_nasa_image_gallery.getAllFavouritesByUser(request)  ##Importamos la lista de favoritos del usuario de "services_nasa_image_gallery"
    ##Ya que necesitaremos usar ambas listas en diferentes ocaciones, añadimos un segundo parámetro (x) para nuestra función, que nos marque cuándo devolver cada lista (Especificado en "def Home(request)")
    if x==1:
        return images
    elif x==0:
        return favourite_list



# función principal de la galería.
def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].
    images = []
    favourite_list = []
    #Llamamos a la función anterior, y establecemos el segundo parámetro como "1", para tomar los elementos de la lista "images" y agregarlos a nuestra nueva lista
    for elem in getAllImagesAndFavouriteList(request,1):
        images.append(elem)
    #Llamamos a la función anterior, y establecemos el segundo parámetro como "0", para tomar los elementos de la lista "favourite_list" y agregarlos a nuestra nueva lista
    for elem in getAllImagesAndFavouriteList(request,0):
        favourite_list.append(elem)
    
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list} )


# función utilizada en el buscador.
def search(request):
    images, favourite_list = getAllImagesAndFavouriteList(request)
    search_msg = request.POST.get('query', '')

    # si el usuario no ingresó texto alguno, debe refrescar la página; caso contrario, debe filtrar aquellas imágenes que posean el texto de búsqueda.
    pass


# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    pass


@login_required
def deleteFavourite(request):
    pass


@login_required
def exit(request):
    pass