# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from ..transport.transport import getAllImages as fetch_raw_images
from django.contrib.auth import get_user 
import requests  

def getAllImages(input=None):
    try:
        raw_images = fetch_raw_images(input=input)
        images = []

        for character in raw_images:
            first_episode_url = character.get("episode", [])[0] if character.get("episode") else None
            first_seen = "Desconocido"
            if first_episode_url:
                first_seen = get_episode_name(first_episode_url) 

            card = {
                "url": character.get("image", ""),
                "name": character.get("name", "Desconocido"),
                "status": character.get("status", "Desconocido"),
                "last_location": character.get("location", {}).get("name", "Desconocido"),
                "first_seen": first_seen  # Usamos el nombre del episodio, no la URL
            }
            images.append(card)

        return images
    except Exception as e:
        print(f"[services.py]: Error al obtener imágenes: {e}")
        return []
import requests

def get_episode_name(episode_url):
    try:
        response = requests.get(episode_url)
        if response.status_code == 200:
            episode_data = response.json()
            return episode_data.get('name', 'Desconocido')  
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el episodio: {e}")
    return "Desconocido"  


# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = ''  # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

 

def getAllFavourites(request):
    if not request.user.is_authenticated:
        return [] 

    user = get_user(request)  
    favourite_list = repositories.getAllFavourites(user)  # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').

    mapped_favourites = []
    for favourite in favourite_list:
        # transformamos cada favorito en una Card, y lo almacenamos en card.
        card = {
            "id": favourite["id"],
            "url": favourite["url"],
            "name": favourite["name"],
            "status": favourite["status"],
            "last_location": favourite["last_location"],
            "first_seen": favourite["first_seen"],
        }
        mapped_favourites.append(card)  

    return mapped_favourites


def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.