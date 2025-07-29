import os
from modulos.menu import cargar_menu
#Variables para crear un juego
WIDTH_MAPA = 30
HEIHT_MAPA= 20
espacio_vacio = "   "
espacio_lleno= "[ ]"

    coordenada_personaje = [8,10]:
    personaje = "ᐅ"

def cargar_mapa(movimiento_personaje):

    # Menú
    cargar_menu()

    os.system("clear")
    if movimiento_personaje == "w":
        personaje = "▲"
        coordenada_personaje[0] -= 1
    elif movimiento_personaje == "s":
        personaje = "▼"
        coordenada_personaje[0] += 1

    print("+"+"-"*90 + "+")
    for cada_fila in range(HEIHT_MAPA):
        print("|", end="")
        for cada_bloque in range(WIDTH_MAPA):
            if(coordenada_personaje[0]==cada_fila and coordenada_personaje[1]== cada_bloque):
             print(f"{cada_bloque}" ,end="")
            else:
                print(espacio_vacio,end="")

    print("|")
    print("+"+"-"*90 + "+")



        