import os
import msvcrt

# Dimensiones del mapa
WIDTH_MAPA = 10
HEIGHT_MAPA = 10

espacio_vacio = "   "
espacio_lleno = "[ ]"


coordenada_personaje = [0,0]  # Coordenadas del personaje (fila, columna)
personaje = "😃"

def cargar_mapa(movimiento_personaje=""):
    global coordenada_personaje

    # Movimiento
    if movimiento_personaje == "w" and coordenada_personaje[0] > 0:
        coordenada_personaje[0] = coordenada_personaje[0] - 1
    elif movimiento_personaje == "s" and coordenada_personaje[0] < HEIGHT_MAPA - 1:
        coordenada_personaje[0] += 1
    elif movimiento_personaje == "a" and coordenada_personaje[1] > 0:
        coordenada_personaje[1] -= 1
    elif movimiento_personaje == "d" and coordenada_personaje[1] < WIDTH_MAPA - 1:
        coordenada_personaje[1] += 1

    # Dibujar mapa
    os.system("cls")  # Limpiar pantalla (en Linux usar 'clear')
    print("+" + "-" * (WIDTH_MAPA * len(espacio_vacio)) + "+")

    for fila in range(HEIGHT_MAPA):
        print("|", end="")
        for columna in range(WIDTH_MAPA):
            if [fila, columna] == coordenada_personaje:
                print(personaje, end="")
            else:
                print(espacio_vacio, end="")
        print("|")

    print("+" + "-" * (WIDTH_MAPA * len(espacio_vacio)) + "+")

# Bucle principal del juego
while True:
    cargar_mapa()
    print("Usa W A S D para mover, Q para salir.")
    tecla = msvcrt.getch().decode("utf-8").lower()

    if tecla == "q":
        break

    cargar_mapa(tecla)
