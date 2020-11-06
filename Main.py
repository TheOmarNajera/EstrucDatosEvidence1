import sys
import os
from functions.directorio import directorio

cut = "\n" + "_"*100 + "\n"
usuario = input("¿Cuál es tu nombre? ")
dirnew = "Escriba el directorio a donde quiera ir (ej. C:\\users\\example): "

print(f"\n¡Hola {usuario}! ¿Qué deseas hacer?")

while True:
    print(f"""
Menú principal
El directorio actual es: {os.getcwd()}
¿Qué desea hacer?
1.- Cambiar el directorio de trabajo.
2.- Escoger un archivo.
3.- Salir.
""")
    op = input("Insertar opción: ")

#----- Opcion 3 / Salir -----------------------    
    if op == "3":
        print(f"\n¡Hasta pronto {usuario}!")
        break

#------- Opción 1 / Cambiar directorio de trabajo ----------------------------------------------------------------------------
    elif op == "1":
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

#------- Opción 2 / Escoger un archivo ------------------------------------------------------------------------------------------------------                
    elif op == "2":
        print(f'\nEl directorio actual es: {os.getcwd()}{cut}') 
        b = directorio(nowdir=os.getcwd()).showfile() #usamos la user defined function que crea una lista de los archivos
        n = []
        for i in b: #se filtran los archivos dejando entrar a la lista vacía solo los archivos y no las carpetas con la funcion isfile de os
            if os.path.isfile(i) == True:
                n.append(i)

        con = 0
        print("Archivos de tu carpeta: ")

        if len(n) > 0: 
            for a in n: #se enumera cada valor de la lista ya filtrada, para que ya enumarados el usuario pueda escogerlo proporcionando un numero
                con += 1
                print(f"{con}: {a}")

            try:
                archi = int(input("\nSeleccione un archivo de la anterior lista: "))
                archivo = n[(archi-1)]

                while True:
                    op2 = input("¿Qué deseas hacer?\n1. Copiar Archivo (reescribirá si un archivo igual se encuentra ahí) \n2. Mover Archivo (si se encuentra un archivo igual, no podrás moverlo a esa ubicacion)) \n")
                    move = input(dirnew)

                    if os.path.exists(move): # Se valida si existe el directorio

                        #- Opción 1 / Copiar Archivo --------------------------------------------------------------------------------------
                        if op2 == "1":
                            directorio(newdir=move,arcsel=archivo).copy() #se usa la UDF copy la cual usa la función copy del modulo shutil
                            break

                        #- Opción 2 / Mover Archivo ---------------------------------------------------------------------------------------
                        elif op2 == "2":
                            directorio(newdir=move,arcsel=archivo).move() #se usa la UDF copy la cual usa la función move del modulo shutil
                            break

                        else:
                            print(f"Opción {op2} no válida.")

                    else:
                        print("No existe el directorio a cambiar.")     
            except:
                print(f"Ocurrió un problema {sys.exc_info()[0]}")
                Excepcion = sys.exc_info()
                for elemento in Excepcion:
                    print(elemento)
        else:
            print("No hay archivos en la carpeta actual.")
    else:
        print(f"La opción '{op}' no es válida.\nEliga una de las opciones correctas.{cut}")