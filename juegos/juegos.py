import os  
import readchar
from mapa import cargar_mapa


estado_juego = true

def cargar_juego():
    # Iniciar juego 
    tecla = readchar.readchar()

    if tecla == "w":
        cargar_mapa(tecla)

    elif tecla == "s":
        cargar_mapa(tecla)

    elif tecla == "a":
        cargar_mapa(tecla)

    elif tecla == "d":
        cargar_mapa(tecla)
    elif tecla == "q":
        estado_juego = False

while estado_juego:
    cargar_juego()

     
    