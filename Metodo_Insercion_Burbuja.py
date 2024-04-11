# Cristian Armando Larios Bravo
# Haciendo y probando codigos chidos

# Metodo de insercion
import random
import numpy as np

""" def buscar_indice(id:int,ids:list)->int: 
    if id in ids:
        return ids.index(id) """

lista  = np.zeros(500)
for i in range(0, 500):
    lista[i] = random.randrange(1,500)
# lista.sort()

# print(lista)
print("##### Ordenamiento por insercion. #####")

for i in range(1,len(lista)):
    aux = lista[i]
    k = i-1
    while k>=0 and aux<lista[k]:
        lista[k+1] = lista[k]
        k = k-1
    lista[k+1] = aux

print(lista)

print("\n\n#### Ordenamiento por metodo de burbuja 3 ####")
lista2 = np.zeros(500)
for i in range(0,500):
    lista2[i] = random.randrange(1,500)
i = 1
Band = False
while i <= len(lista2)-1 and Band == False :
    Band = True
    for j in range(0,len(lista2)-1):
        if lista2[j]>lista2[j+1]:
            aux2 = lista2[j]
            lista2[j] = lista2[j+1]
            lista2[j+1] = aux2
            Band = False
lista2
print(lista2)



print("\n\n#### Ordenamiento por metodo de burbuja Funcion ####")

lista3 = np.zeros(500)
for i in range(0,500):
    lista3[i] = random.randrange(1,500)

def DeLaBurbuja(a2):
    for i in range(1,len(a2)):
        for j in range(0,len(a2)-1):
            if a2[j] > a2[j+1]:
                aux = a2[j]
                a2[j] = a2[j+1]
                a2[j+1] = aux

DeLaBurbuja(lista3)
print(lista3)
