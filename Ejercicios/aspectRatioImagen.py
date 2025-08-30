import math
import requests
from PIL import Image
from io import BytesIO

url = 'https://wallpapers.com/images/hd/1920x1080-pictures-zog2vma3qpmt2o9l.jpg'

try:
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    imagen_bytes = BytesIO(respuesta.content)
    imagen = Image.open(imagen_bytes)


except requests.exceptions.RequestException as e:
    print(f"Error al descargar la imagen: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")

    copiaImg = imagen

def simplificar (x,y):
    if y == 0:
        return "error !!!! no se divide entre 0"
    abs_x = abs(x)
    abs_y = abs(y)
    mcd = math.gcd(abs_x,abs_y)
    x = x//mcd
    y=y//mcd
    return [x,y]

print("Relacion de aspecto ",simplificar(imagen.size[0],imagen.size[1])) #.size regresa una tupla (x,y)