# Configuración del sistema

# Versión del trabajo práctico
VERSION = "Trabajo práctico - 2do cuatrimestre del 2024."


BASE_API_URL = "https://rickandmortyapi.com/api/character"

# Rick & Morty REST API para capturar imágenes de la galería
DEFAULT_PAGE = 1  

# Palabra buscada por defecto.
DEFAULT_NAME_QUERY_PARAM = "name"

# URLs 
DEFAULT_REST_API_URL = f"{BASE_API_URL}?page={DEFAULT_PAGE}"
DEFAULT_REST_API_SEARCH = f"{BASE_API_URL}?page={DEFAULT_PAGE}&{DEFAULT_NAME_QUERY_PARAM}="