import sys
import os
from functions.directorio import directorio
import time  
from os import system,name
def limpiar():
    if name == "nt":
        system("cls")
    else:
        system("clear")

cut = "\n" + "_"*100 + "\n"
sepa = ('~'*40)
limpiar()
usuario = input("¿Cuál es tu nombre? ")
limpiar()
dirnew = "Escriba el directorio a donde quiera ir (ej. C:\\users\\example): "

print(f"\n   ¡Hola {usuario}! ¿Qué deseas hacer?")
historial = []
conh = 0
while True:
    print(f"""
{sepa}
          Menú principal\n
        ¿Qué desea hacer?\n
1.- Cambiar el directorio de trabajo.
2.- Escoger un archivo.
3.- Salir.
4.- Ver historial
{sepa}\n
El directorio actual es: {os.getcwd()}S
""")
    op = input("Insertar opción: ")

#----- Opcion 3 / Salir -----------------------    
    if op == "3":
        limpiar()
        print(f"\n¡Hasta pronto {usuario}!")
        break

#------- Opción 1 / Cambiar directorio de trabajo ----------------------------------------------------------------------------
    elif op == "1":
        user = input(dirnew)

        if user == os.getcwd():
            print("Esta tratando de ir al directorio donde se encuentra actualmente")

        else:
            try:
                limpiar()
                print(f"El directorio '{os.getcwd()}' cambiará a '{user}'\n")
                diruser = directorio(newdir=user)
                diruser.changedir()
                print(f"\nEl directorio cambio correctamente. \nEl directorio actual es: {os.getcwd()}{cut}")
                conh += 1
                f = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                historial.append(f'({conh}) {f}: Se cambio el directorio a {user}')
                
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
        limpiar()
        if op == '2':
            la = input('\n1.Ver el listado con proceso de listas\n2.Ver el listado con proceso de tuplas\n:')
            limpiar()
            con = 0
            z = 'n'
            if la == '1':
                tipo = 'lista'
                z = 'm'
            elif la == '2':
                tipo = 'tupla'
                n = tuple(n)
                z = 'm'

            print("\nArchivos de tu carpeta: ")
            
            if z == 'm':
                if len(n) > 0:
                    Tiempo = time.time() 
                    for a in n: #se enumera cada valor de la lista ya filtrada, para que ya enumarados el usuario pueda escogerlo proporcionando un numero
                        con += 1
                        print(f"({con}): {a}")
                    Tiempo = time.time() - Tiempo
                    print(f"\nLa {tipo} tiene {len(n)} elementos, y tiene un tamaño de {sys.getsizeof(n)} bytes y se tardo {Tiempo}\n")
                    try:
                        archi = int(input("\nSeleccione el indice mostrado de su archivo de la anterior lista: "))
                        archivo = n[(archi-1)]
                        limpiar()
                        while True:
                            op2 = input("¿Qué deseas hacer?\n1. Copiar Archivo (reescribirá si un archivo igual se encuentra ahí) \n2. Mover Archivo (si se encuentra un archivo igual, no podrás moverlo a esa ubicacion)) \n")
                            move = input(dirnew)

                            if os.path.exists(move): # Se valida si existe el directorio

                                #- Opción 1 / Copiar Archivo --------------------------------------------------------------------------------------
                                if op2 == "1":
                                    directorio(newdir=move,arcsel=archivo).copy() #se usa la UDF copy la cual usa la función copy del modulo shutil
                                    conh += 1
                                    f = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                                    historial.append(f'({conh}) {f}: Se copio el archivo {archivo} en el destino {move}')
                                    limpiar()
                                    print('\nSe copio exitosamente')
                                    break

                                #- Opción 2 / Mover Archivo ---------------------------------------------------------------------------------------
                                elif op2 == "2":
                                    directorio(newdir=move,arcsel=archivo).move() #se usa la UDF copy la cual usa la función move del modulo shutil
                                    conh += 1
                                    f = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                                    historial.append(f'({conh}) {f}: Se movio el archivo {archivo} en el destino {move}')
                                    limpiar()
                                    print('\nSe copio exitosamente')
                                    break

                                else:
                                    limpiar()
                                    print(f"Opción {op2} no válida.")

                            else:
                                limpiar()
                                print("No existe el directorio a cambiar.")     
                    except:
                        limpiar()
                        print(f"Ocurrió un problema {sys.exc_info()[0]}")
                        Excepcion = sys.exc_info()
                        for elemento in Excepcion:
                            print(elemento)
                else:
                    limpiar()
                    print("No hay archivos en la carpeta actual.")
            else:
                limpiar()
                print('La opcion no es valida')
    elif op == '4':
        limpiar()
        print ('       Historial')
        for k in historial:
            print(k)      
    else:
        limpiar()
        print(f"La opción '{op}' no es válida.\nEliga una de las opciones correctas.{cut}")