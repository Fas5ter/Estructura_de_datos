# Cristian Armando Larios Bravo
# Haciendo y probando codigos chidos
from random import randint, uniform, random
import time

class Pila:
    def __init__(self):
        self.items = []

    def PilaVacia(self):
        return self.items == []

    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        return self.items.pop()

    def Verificar(self):
        return self.items(len(self.items)-1)

    def tamano(self):
        return len(self.items)

    def TLlegada(self):
        Tiempo = randint(0,3)
        return Tiempo

    def TAtn(self):
        Tiempo = randint(0,3)
        return Tiempo

    def Cual(self):
        return randint(1,2)

if __name__ == '__main__':
    
    num = 1
    x  = Pila()

    while True:
        if x.Cual() == 1:
            time.sleep(x.TLlegada())
            x.Push(num)
            num+=1
            time.sleep(x.TAtn())
        else:
            if x.PilaVacia() == True:
                time.sleep(x.TLlegada())
                num+=1
                print("Lista vacia")
                time.sleep(x.TAtn())
            else:
                time.sleep(x.TLlegada())
                num+=1
                x.Pop()
                time.sleep(x.TAtn())
        print(x.items)            