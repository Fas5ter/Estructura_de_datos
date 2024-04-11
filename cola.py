# Cristian Armando Larios Bravo
# Haciendo y probando codigos chidos
from random import randint, uniform, random
import time

class Cola:
    '''
    Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado
    '''

    def __init__(self):
        # Crea una cola vacia
        # La cola vacia se representa por una lista vacia
        self.items = []



    def encolar(self, x):
        # Agrega el elemento x como ultimo de la cola.
        self.items.append(x)

    def desencolar(self):
        '''
        Elimina el primer elemento de la cola y devuelve su valor. Si la cola esta vacia,
        levanta ValueError.
        '''
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")
    
    def es_vacia(self):
        # Devuelve True si la cola esta vacia, False si no.
        return self.items == []
    
    def TLlegada(self):
        Tiempo = randint(0, 2)
        return Tiempo
    
    def TAtn(self):
        Tiempo = randint(0, 2)
        return Tiempo
    
    def Cual(self):
        return randint(1,2)
    
if __name__ == '__main__':
    num = 1
    col = Cola()

    while True:
        if col.Cual() == 1:
            time.sleep(col.TLlegada())
            col.encolar(num)
            num+=1
            time.sleep(col.TAtn())
        else:
            if col.es_vacia() == False:
                time.sleep(col.TLlegada())
                col.desencolar()
                num+=1
                time.sleep(col.TAtn())
        print(col.items)