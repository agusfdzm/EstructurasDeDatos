class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# nodo1 = Nodo(1)
# nodo2 = Nodo(2)
# nodo3 = Nodo(3)

# nodo1.siguiente = nodo2
# nodo2.siguiente = nodo3
# nodo3.siguiente = None

class LinkedList:
    def __init__(self):
        self.cabeza = None

    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")
