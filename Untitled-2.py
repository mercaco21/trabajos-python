class Alumno:
    def __init__(self, nombre, apellido, dni, legajo, carrera, email,fecahaingrsofacultad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.legajo = legajo
        self.carrera = carrera  
        self.email = email
        self.fechaingresofacultad = fecahaingrsofacultad
        

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

#Carrera : carrera en que  cursa el alumno , solo un string.

class Materia:
    def __init__(self, nombre, comision, anio_carrera):
        
        self.nombre = nombre
        self.comision = comision
        self.anio_carrera = anio_carrera 

    def cambiar_comision(self, nuevo_comision):
        self.comision = nuevo_comision

    def cambiar_anio_carrera(self, nuevo_anio_carrera):
        self.anio_carrera = nuevo_anio_carrera

    def mostrar_info(self):
        print("\n=== Información de la Materia ===")
        print(f"Nombre: {self.nombre}")
        print(f"comision: {self.comision}")
        print(f"Se cursa en: {self.anio_carrera}")

   