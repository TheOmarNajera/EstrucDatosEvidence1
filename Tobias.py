import sys

elementos=[]
SEPARADOR=("*"*40)

print("*"*20,"Bienvenido","*"*20)
print("PROGRAMA PARA LA REVELECION DE BYTES OCUPADOS EN MEMORIA MAS TIEMPO DE EJECUCION")
while True:
    menu=int(input("1:Agregar elemento\n2:Ver tamaño de memoria en LISTA\n3:Ver tamaño de memoria en Tupla\n4:SALIR\n"))
    if menu == 1:
        a=input("Dame un nombre: ")
        elementos.append(a)
        input("Elemento agregado,presiona enter\n")
        print(SEPARADOR)
        pass
    elif menu == 2:
        if elementos == []:
            input("Tienes que agregar elementos")
            print(SEPARADOR)
        else:
            print(f"La lista tiene {len(elementos)} elementos, y tiene un tamaño de {sys.getsizeof(elementos)} bytes")
            print(SEPARADOR)
            pass
    elif menu == 3:
        if elementos == []:
            input("Tienes que agregar elementos")
            print(SEPARADOR)
        else:
            tupla = tuple(elementos)
            print(f"La tupla tiene {len(tupla)} elementos, y tiene un tamaño de {sys.getsizeof(tupla)} bytes")
            print(SEPARADOR)
            pass
    elif menu == 4:
        print("GARCIAS POR USAR EL PROGRAMA")
        break
    
