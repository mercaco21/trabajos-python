#-------- Clase Anidada - NODO ------------#
class Node:

        def init(self, element, next):
            self._element = element # inicializar el contenido del Nodo
            self._next = next       #referencia al siguiente Nodo
#Implementar una Pila

class ListaSimpleEnlazada:
    """Clase Lista 'Simplemente' Enlazada."""

    def init(self):
        """Crea una Pila Vacia."""
        self._head = None  #referencia a la "cabeza" de la lista
        self._size = 0     #cantidad de elementos


    def len(self):
        """Retorna el numero de elementos de la Pila."""
        return self._size

    def is_empty(self):
        """Retorna VERDADERO si la Pila esta Vacia."""
        return self._size == 0

    #----------- MÃ©todos de la Pila ----------- #


    def push(self, elem):
        nuevo_nodo = Node(elem, self._head)
        self._head = nuevo_nodo
        self._size +=1

    def pop(self):
        if self._size == 0:
            return None
        temp = self._head._element 
        self._head = self._head._next
        self._size -=1
        return temp

    def top(self):
        if self._size == 0:
            return None
        return self._head._element


escuderia=ListaSimpleEnlazada()

escuderia.push('Red Bull Racing')
escuderia.push('Mercedes-AMG Petronas')
escuderia.push('Scuderia Ferrari')
escuderia.push('McLaren F1 Team')
escuderia.push('Aston Martin Aramco')
escuderia.push('Alpine F1 Team')
escuderia.push('Williams Racing')
escuderia.push('Stake F1 Team Kick Sauber')
escuderia.push('Visa Cash App RB')
escuderia.push('Haas F1 Team')

print(len(escuderia))
print(escuderia.pop())
print(escuderia.top())