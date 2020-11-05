import sys
import os
from functions.directorio import directorio

cut = "\n" + "_"*50 + "\n"
usuario = input("¿Cuál es tu nombre? ")

dirnew = "Escriba el directorio (ej. C:\\users\\example): "

print(f"\n¡Hola {usuario}! ¿Qué deseas hacer?\n")


while True:
    print("""Menú principal
1.- Consultar su directorio actual.
2.- Cambiar el directorio de trabajo.
3.- Escoger un archivo.
4.- Salir.
""")
    op = input("Insertar opción: ")
    
    if op == "4":
        print(f"\n¡Hasta pronto {usuario}!")
        break

    elif op == "1":
        print(f'\nEl directorio actual es: {os.getcwd()}{cut}')

    elif op == "2":
        user = input(dirnew)

        if user == os.getcwd():
            print("Esta tratando de ir al directorio donde se encuentra actualmente")

        else:
            try:
                print(f"El directorio '{os.getcwd()}' cambiará a '{user}'\n")
                diruser = directorio(newdir=user)
                diruser.changedir()
                print(f"\nEl directorio cambio correctamente. \nEl directorio actual es: {os.getcwd()}{cut}")
                
            except:
                print("Directorio Inválido. Intente de nuevo.")
                
    elif op == "3":
        print(f'\nEl directorio actual es: {os.getcwd()}{cut}')
        n = directorio(nowdir=os.getcwd()).showfile()
        con = 0
        print("Archivos de tu carpeta: ")

        if len(n) > 0:

            for a in n:
                con += 1
                print(f"{con}: {a}")

            try:
                archi = int(input("\nSeleccione un archivo de la anterior lista: "))

                if (archi - 1) in range(len(n)):
                    archivo = n[(archi-1)]

                    while True:
                        op2 = input("¿Qué deseas hacer?\n1. Copiar Archivo\n2. Mover Archivo\n")
                        move = input(dirnew)
    
                        try:
                            if op2 == "1":
                                directorio(newdir=move,arcsel=archivo).copy()
                                break

                            elif op2 == "2":
                                directorio(newdir=move,arcsel=archivo).move()
                                break

                            else:
                                print(f"Opción {op2} no válida.")

                        except:
                            print("No existe el directorio a cambiar.")     

                else:
                    print(f"No hay archivo número {archi}.")

            except:
                print(f"Ocurrió un problema {sys.exc_info()[0]}")
                Excepcion = sys.exc_info()

                for elemento in Excepcion:
                    print(elemento)
            
        else:
            print("No hay archivos en la carpeta actual.")

    else:
        print(f"La opción '{op}' no es válida.\nEliga una de las opciones correctas.{cut}")