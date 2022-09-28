from Nodo import *
class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
    
    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)  

    # Método para verificar si la estructura de datos esta vacia
    def vacio(self):
        return self.cabeza == None

    # Método para agregar elementos al final de la linked list
    def agregar_al_final(self, dato):
        if not self.cabeza:
            self.cabeza = Nodo(dato=dato)
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=dato)
    
    # Método para eleminar nodos
    def borrar_nodo(self, key):
        actual = self.cabeza
        temporal = None
        while actual and actual.dato != key:
            temporal = actual
            actual = actual.siguiente
        if temporal is None:
            self.cabeza = actual.siguiente
        elif actual:
            temporal.siguiente = actual.siguiente
            actual.siguiente = None

    # Método para obtener el ultimo nodo
    def obtener_ultimo_nodo(self):
        temp = self.cabeza
        while(temp.siguiente is not None):
            temp = temp.siguiente
        return temp.dato

    

        