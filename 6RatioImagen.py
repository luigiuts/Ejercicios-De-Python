from PIL import Image
import requests

def calcular_aspect_ratio(url):
    try:
        # Descargar la imagen desde la URL
        imagen = Image.open(requests.get(url, stream=True).raw)
        
        # Obtener las dimensiones de la imagen
        ancho, alto = imagen.size
        
        # Calcular el aspect ratio
        aspect_ratio = ancho / alto
        
        # Redondear el aspect ratio a dos decimales
        aspect_ratio = round(aspect_ratio, 2)
        
        return aspect_ratio
    except Exception as e:
        return f"Error: {e}"

# URL de ejemplo
url_ejemplo = "https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png"

# Calcular el aspect ratio
aspect_ratio = calcular_aspect_ratio(url_ejemplo)
print("Aspect ratio:", aspect_ratio)
