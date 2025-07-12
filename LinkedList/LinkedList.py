from dataclasses import dataclass

@dataclass
class Node:
    value: int
    nextNode: "Node"

class LinkedList:
    _size: int
    _firstNode: Node

    def __init__(self) -> None:
        self._size = 0
        self._firstNode = None

    def add(self, position: int, element: int):
        if position == 0:
            self._firstNode = Node(value=element, nextNode=self._firstNode)
        else:
            currentNode = self._firstNode
            for _ in range(0, position - 1):
                currentNode = currentNode.nextNode
            currentNode.nextNode = Node(
                value=element, nextNode=currentNode.nextNode
            )

        self._size += 1

    def delete(self, position: int):
        if position == 0:
            self._firstNode = self._firstNode.nextNode
        else:
            currentNode = self._firstNode
            for _ in range(0, position - 1):
                currentNode = currentNode.nextNode
            currentNode.nextNode = currentNode.nextNode.nextNode

    def get(self, position: int) -> int:
        currentNode = self._firstNode
        for _ in range(0, position):
            currentNode = currentNode.nextNode
        return currentNode.value
    
    def recibirTamaño(self) -> int:
        return self._size
    
lista = LinkedList()
lista.add(0, 1)
lista.add(1, 10)
lista.add(2, 20)
lista.add(3, 30)

print(lista.recibirTamaño())



























# class Nodo:
#     def __init__(self, dato):
#         self.dato = dato
#         self.siguiente = None

# # nodo1 = Nodo(1)
# # nodo2 = Nodo(2)
# # nodo3 = Nodo(3)

# # nodo1.siguiente = nodo2
# # nodo2.siguiente = nodo3
# # nodo3.siguiente = None

# class LinkedList:
#     def __init__(self):
#         self.cabeza = None

#     def agregar_al_inicio(self, dato):
#         nuevo = Nodo(dato)
#         nuevo.siguiente = self.cabeza
#         self.cabeza = nuevo

#     def mostrar(self):
#         actual = self.cabeza
#         while actual:
#             print(actual.dato, end=" -> ")
#             actual = actual.siguiente
#         print("None")
