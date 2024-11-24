# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    images = services.getAllImages()
    favourite_list = services.getAllFavourites(request)
    favourite_urls = {fav["url"] for fav in favourite_list}
    for img in images:
        img["is_favourite"] = img["url"] in favourite_urls

    return render(request, "home.html", {"images": images})

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).
    if (search_msg != ''):
        pass
    else:
        return redirect('home')
    
def get_episode_name(episode_url):
    response = requests.get(episode_url)
    if response.status_code == 200:
        episode_data = response.json()
        return episode_data['name']
    return "Desconocido" 

def home_view(request):
    images = services.get_episode_name
    for img in images:
        if img.first_seen:
            img.first_seen = get_episode_name(img.first_seen)

    return render(request, 'home.html', {'images': images})

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    pass