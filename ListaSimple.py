from Nodo import *
class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
        self.ultimo = None 
        self.size = 0
    
    def vacio(self):
        return self.cabeza == None

    def agregar_al_final(self, dato):
        if self.vacio():
            self.cabeza = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size +=1

    def size(self):
        return self.size
    def vaciar(self):
        self.cabeza=None
    

        