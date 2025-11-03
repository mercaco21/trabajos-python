
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza=nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente=nuevo_nodo

    def eliminar(self, valor):
        if self.cabeza is None:
            return
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return
        
        nodo_actual = self.cabeza
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            nodo_actual = nodo_actual.siguiente

    def buscar(self, valor):
        nodo_actual = self.cabeza
        while nodo_actual.siguiente is not None:
            if nodo_actual.valor == valor:
                return True
            nodo_actual = nodo_actual.siguiente
        return False        


class Persona:
    def __init__(self, nombre,peliculas,):
      self.nombre = nombre
      self.peliculas = peliculas
      self.colecciones = []

class Pelicula:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio
        self.peliculas = []
        # self.peliculas = peliculas
        # self.anio = anio_in_peliculas

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


    def alquilar_coleccion(self, coleccion):
        self.colecciones.append(coleccion)

    def ver_todas_las_peliculas(self):
        print(f"\n{self.nombre} va a ver las películas ordenadas por año:")
        for coleccion in self.colecciones:
            coleccion.mostrar_peliculas_ordenadas()
            
        for coleccion in self.colecciones:
            print(f"{coleccion.nombre} - {coleccion.anio}")



class ColeccionPeliculas:
    def __init__(self, topico):
        self.topico = topico
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def obtener_peliculas_ordenadas(self):
        return sorted(self.peliculas, key=lambda p: p.anio)

    def mostrar_peliculas_ordenadas(self):
        print(f"\nPelículas sobre el tópico: {self.topico}")
        for pelicula in self.obtener_peliculas_ordenadas():
            print(" -", pelicula)


# Clase que representa una persona que recibe y ve las películas

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.colecciones = []

    def recibir_coleccion(self, coleccion):
        self.colecciones.append(coleccion)

    def ver_todas_las_peliculas(self):
        print(f"\n{self.nombre} va a ver las películas ordenadas por año:")
        for coleccion in self.colecciones:
            coleccion.mostrar_peliculas_ordenadas()


# -------------------------------

# -------------------------------

# Crear películas
p1 = Pelicula("los caballeros", 1972)
p2 = Pelicula("Star Wars", 1975)
p3 = Pelicula("las lomas ", 2011)
p4 = Pelicula("ete", 2014)
p5 = Pelicula("el feo y el malo ", 1982)

# Crear colección con tópico: Accion
coleccion_scifi = ColeccionPeliculas("Accion")
coleccion_scifi.agregar_pelicula(p1)
coleccion_scifi.agregar_pelicula(p2)
coleccion_scifi.agregar_pelicula(p3)
coleccion_scifi.agregar_pelicula(p4)
coleccion_scifi.agregar_pelicula(p5)

# Crear otra colección: Viajes en el tiempo
coleccion_tiempo = ColeccionPeliculas("Viajes ")
coleccion_tiempo.agregar_pelicula(Pelicula("Bolver al futuro", 1985))
coleccion_tiempo.agregar_pelicula(Pelicula("Julio verne ", 2012))
coleccion_tiempo.agregar_pelicula(Pelicula("el espejo del tiempo", 1995))

# Crear persona y asignar colecciones
persona1 = Persona("Lautaro")
persona1.recibir_coleccion(coleccion_scifi)
persona1.recibir_coleccion(coleccion_tiempo)


pelicula1 = Pelicula("los caballeros", 1972)
pelicula2 = Pelicula("Star Wars", 1975)
pelicula3 = Pelicula("el feo y el malo", 1982)

# Guardamos en una lista
peliculas = [pelicula1, pelicula2, pelicula3]

# Mostramos los datos ordenados
for peli in sorted(peliculas, key=lambda p: p.anio):
    print(peli)
# Ver las películas en orden

persona1.ver_todas_las_peliculas()







