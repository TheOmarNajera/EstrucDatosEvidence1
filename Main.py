import sys
import os
import shutil

cut = "\n" + "_"*50 + "\n"
usuario = input("¿Cuál es tu nombre? ")

print(f"\n¡Hola {usuario}! ¿Qué deseas hacer?\n")

while True:
    print("""Menú principal
1.- Consultar su directorio actual.
2.- Cambiar el directorio de trabajo.
3.- Escoger un archivo.
4.- Salir.
""")
    op = input("Insertar opción: ")
    
    if op == "1":
        print(f'\n El directorio actual es: {os.getcwd()}{cut}')
    elif op == "2":
        print(f"EJECUTASTE 2{cut}")
        pass
    elif op == "3":
        print(f"EJECUTASTE 3{cut}")
    elif op == "4":
        print(f"\n¡Hasta pronto {usuario}!")
        break
    else:
        print(f"La opción '{op}' no es válida.\nEliga una de las opciones correctas.{cut}")