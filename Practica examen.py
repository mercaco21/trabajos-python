class Alumno:
    def __init__(self, nombre, apellido, dni, legajo, carrera, email,fecahaingrsofacultad, str):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.legajo = legajo
        self.carrera = carrera  
        self.email = email
        self.fechaingresofacultad = fecahaingrsofacultad
        self.materias = []  # lista de materias (objetos Materia)
        self.materias_aprobadas = []  # lista de códigos de materias aprobadas
        self.profesores_cursados = None  # inicio de lista enlazada
        self.str=[] # str
       


        def cambiar_nombre(self, nuevo_nombre):
          self.nombre = nuevo_nombre

        def cambiar_apellido(self, nuevo_apellido):
          self.apellido = nuevo_apellido

        def cambiar_dni(self, nuevo_dni):
          self.dni = nuevo_dni

        def cambiar_legajo(self, nuevo_legajo):
          self.legajo = nuevo_legajo

        def cambiar_carrera(self, nueva_carrera):  
          self.carrera = nueva_carrera

        def cambiar_email(self, nuevo_email):   
          self.email = nuevo_email

        def cambiar_fechaingresofacultad(self, nuevo_fechaingresofacultad):   
          self.fechaingresofacultad = nuevo_fechaingresofacultad


        def recibir_mensaje(self, mensaje):
          print(f" Mensaje para {self.nombre} {self.apellido}: {mensaje}")

    
        def mostrar_datos(self):
          print("\n=== Datos del Alumno ===")
          print(f"Nombre: {self.nombre}")
          print(f"Apellido: {self.apellido}")
          print(f"DNI: {self.dni}")
          print(f"Legajo: {self.legajo}")
          print(f"Carrera: {self.carrera}")
          print(f"Email: {self.email}")


          def asignar_materia(self, materia):
            if materia.carrera != self.carrera:
             print(f" No se puede asignar '{materia.nombre}' a {self.nombre}. Otra carrera.")
            else:
             self.materias.append(materia)
             self.materias.sort(key=lambda m: m.comision)  # mantener ordenado para búsqueda
             print(f" Asignada: {materia.nombre} [{materia.comision}]")

    def mostrar_materias(self):
        print(f"\nMaterias asignadas a {self.nombre}:")
        for m in self.materias:
            print(f"- {m.nombre} (Comision: {m.comision})")

    def cursa_materia(self, comision):
        return self._busqueda_binaria_materia(comision) is not None

    def eliminar_materia(self, comision):
        idx = self._busqueda_binaria_materia(comision, return_index=True)
        if idx is not None:
            materia_eliminada = self.materias.pop(idx)
            print(f" Materia eliminada: {materia_eliminada.nombre}")
        else:
            print(" Materia no encontrada.")



#Carrera : carrera en que  cursa el alumno , solo un string.

class Materia:
    def __init__(self, nombre, comision, anio_carrera,cantidad_alumnos,carrera ):
        
        self.nombre = nombre
        self.comision = comision
        self.anio_carrera = anio_carrera 
        self.cantidad_alumnos = cantidad_alumnos
        self.carrera = carrera  #  Nueva: la carrera a la que pertenece
        self.materias = []  #  Nueva lista de materias asignadas



    def cambiar_comision(self, nuevo_comision):
        self.comision = nuevo_comision

    def cambiar_anio_carrera(self, nuevo_anio_carrera):
        self.anio_carrera = nuevo_anio_carrera

    def cambiar_carrera(self, nuevo_carrera):
        self.carrera = nuevo_carrera
    
    def cambiar_cantidad_alumnos(self, nueva_cantidad):
        self.cantidad_alumnos = nueva_cantidad
    
    def cambiar_materia(self, nueva_materia):
        self.materias=nueva_materia
    
    def mostrar_info(self):
        print("\n=== Información de la Materia ===")
        print(f"Nombre: {self.nombre}")
        print(f"comision: {self.comision}")
        print(f"Se cursa en: {self.anio_carrera}")
        print(f"Cantidad de Alumnos: {self.cantidad_alumnos}")
        print(f"Carrera: {self.carrera}")
        print(f"materias: {self.materias}" )
 

    def asignar_materia(self, materia):
        self.materias.append(materia)
        print(f"Materia '{materia.nombre}' asignada a {self.nombre}.")

    def mostrar_materias(self):
        print(f"\nMaterias de {self.nombre} {self.apellido}:")
        if not self.materias:
            print("No tiene materias asignadas.")
        else:
            for mat in self.materias:
                print(f"- {mat.nombre} (Comisión {mat.comision}, Año {mat.anio_carrera})")
  

  




    