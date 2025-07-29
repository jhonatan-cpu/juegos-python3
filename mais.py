# importando el modulo os 
import os
from data.datos import lista_menu
from programas.sumas import sumas2


# limpiar la terminal 
os. system("cls")
sumar2()

estado = True 

# bucle depende de la vatiable estado
while Estado:
    print("+-----------------------------------+")
    print(" |JHONATAN                2025 v.1 | ")
    print("|                                   |")
    print((typelista_menu))
    print(f"| [1]: {lista_menu[0]})")
    print(f"| [1]: {lista_menu[1]})")
    print(f"| [1]: {lista_menu[2]})")
    print(f"| [1]: {lista_menu[3]})")
    print(f"| [1]: {lista_menu[4]})")   
    print(f"|[0]: salir")


# respuera en dato ingresado
r = int(input("|[?]: "))


# preugnta si el dato ingresaso des una de las opciones disponibles 
if r == 0 :
    estado = False  
elif r == 1:
    sumar2()

# limpiar la terminal 
os. system("cls")



# codigo fuera del bucle, se ejecuta si el bucle deja ser verdadero 
print("|[saliendo del programa...]")



from juego.juegos

