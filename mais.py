# Variables para crear un juego
WIDTH_MAPA = 30
HEIGHT_MAPA = 20
espacio_vacio = "  "
espacio_lleno = "[ ]"

coordenada_personaje = [4, 10]
personaje = "😀"

def cargar_mapa(movimiento_personaje):
    global personaje

    # Movimiento hacia arriba
    if movimiento_personaje == "w":
        if coordenada_personaje[0] > 0:
            coordenada_personaje[0] -= 1

    # Movimiento hacia abajo
    elif movimiento_personaje == "s":
        if coordenada_personaje[0] < HEIGHT_MAPA - 1:
            coordenada_personaje[0] += 1

    # Movimiento a la izquierda
    elif movimiento_personaje == "a":
        if coordenada_personaje[1] > 0:
            coordenada_personaje[1] -= 1

    # Movimiento a la derecha
    elif movimiento_personaje == "d":
        if coordenada_personaje[1] < WIDTH_MAPA - 1:
            coordenada_personaje[1] += 1

# Dibujar el mapa
    print("+" + "-" * (WIDTH_MAPA * len(espacio_vacio)) + "+")
    for cada_fila in range(HEIGHT_MAPA):
        print("|", end="")
        for cada_bloque in range(WIDTH_MAPA):
            if coordenada_personaje[0] == cada_fila and coordenada_personaje[1] == cada_bloque:
                print(f"{personaje}", end="")
            else:
                print(espacio_vacio, end="")
        print("|")
    print("+" + "-" * (WIDTH_MAPA * len(espacio_vacio)) + "+")

# Código principal del juego
if _name_ == "_main_":
    while True:
        movimiento = input("Mover personaje (w/a/s/d, q para salir): ").lower()
        if movimiento == "q":
            print("¡Juego terminado!")
            break
        cargar_mapa(movimiento)





