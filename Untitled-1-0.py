class Node:

        def __init__(self, element, next):
            self._element = element # inicializar el contenido del Nodo
            self._next = next       #referencia al siguiente Nodo
#Implementar una Pila

class ListaSimpleEnlazada:
    """Clase Lista 'Simplemente' Enlazada."""

    def __init__(self):
        """Crea una Pila Vacia."""
        self._head = None  #referencia a la "cabeza" de la lista
        self._size = 0     #cantidad de elementos


    def __len__(self):
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
Minimizar
ejercicio01.py
2 KB
Ocultación (encapsulación) y atributos privados:

    Para ocultar una clase interna o un atributo, se utiliza el prefijo doble guión bajo __ antes del nombre.
    Los atributos y clases marcados como privados son inaccesibles directamente desde fuera de la clase contenedora. La intención es que se usen internamente dentro de la clase.
principal = ClasePrincipal()
interna = principal.ClaseInterna(principal)  # Crear instancia de la clase interna
interna.mostrar()
# No puedes acceder directamente a __ClaseInternaOculta
# intento_acceso = principal.__ClaseInternaOculta(principal)  # Esto generarÃ¡