import numpy as np
import random

def busqueda_binaria(lista,num):
    ini = 0
    fin = len(lista)-1

    while ini <= fin:
        mid = (ini + fin) // 2
        if lista[mid] == num:
            return True
        elif lista[mid] < num:
            ini = mid + 1
        elif lista[mid] > num:
            fin = mid - 1
    return False

def busqueda_secuencial(lista, num):
    for i in range(0,len(lista)):
        if num == lista[i]:
            return True
    return False


if __name__ == "__main__":
    Arreglo = np.zeros(500)
    for i in range(0,500):
        Arreglo[i] = random.randrange(1,500)
    Arreglo.sort()
    # print(Arreglo)
    num = int(input("Introduce el numero a buscar: "))
    if busqueda_binaria(Arreglo, num):
        print("El numero esta en la lista")
    else:
        print("El numero no esta en la lista")

    if busqueda_secuencial(Arreglo,num):
        print("El numero esta en la lista")
    else:
        print("El numero no esta en la lista")


