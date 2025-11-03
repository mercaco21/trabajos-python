#----------------------------------------------------------------------------------------------------------------
# Más opciones pidiéndole a La IA que me ayude a sumar más ideas .


# Segundo Ejemplo









# sistema_alumnos.py

import os
import pickle
from collections import deque
from datetime import datetime

class Materia:
    def __init__(self, codigo, nombre, comision, anio_carrera, carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.comision = comision
        self.anio_carrera = anio_carrera
        self.carrera = carrera

class Profesor:
    def __init__(self, nombre, apellido, materia, anio_ingreso):
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia
        self.anio_ingreso = anio_ingreso
        self.sig = None  # Para lista enlazada

    def __str__(self):
        antiguedad = datetime.now().year - self.anio_ingreso
        mensaje_antiguedad = " - Tiene más de 20 años de antigüedad" if antiguedad > 20 else ""
        return f"Profesor: {self.nombre} {self.apellido} | Materia: {self.materia} | Ingreso: {self.anio_ingreso}{mensaje_antiguedad}"

class Alumno:
    def __init__(self, nombre, apellido, dni, legajo, carrera, email, fechaingresofacultad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.legajo = legajo
        self.carrera = carrera
        self.email = email
        self.fechaingresofacultad = fechaingresofacultad
        self.materias = deque()  # fila de materias a cursar
        self.materias_cursando = deque()  # materias en orden de inicio
        self.materias_aprobadas = []  # lista de codigos de materias aprobadas
        self.profesores_cursados = None  # lista enlazada de profesores

    def asignar_materia(self, materia):
        if materia.carrera != self.carrera:
            print(f" No se puede asignar '{materia.nombre}' a {self.nombre}. Otra carrera.")
        else:
            self.materias.append(materia)
            print(f" Asignada: {materia.nombre} [{materia.codigo}]")

    def comenzar_materia(self):
        if self.materias:
            materia = self.materias.popleft()
            self.materias_cursando.append(materia)
            print(f" Comenzando materia: {materia.nombre}")

    def aprobar_materia(self):
        if self.materias_cursando:
            materia = self.materias_cursando.popleft()
            self.materias_aprobadas.append(materia.codigo)
            print(f" Materia aprobada: {materia.nombre}")

    def mostrar_materias(self):
        print(f"\nMaterias en fila para {self.nombre}:")
        for m in list(self.materias):
            print(f"- {m.nombre} (Código: {m.codigo})")

    def cursa_materia(self, codigo):
        return any(m.codigo == codigo for m in self.materias)

    def eliminar_materia(self, codigo):
        self.materias = deque(m for m in self.materias if m.codigo != codigo)

    def verificar_aprobada(self, codigo):
        self.materias_aprobadas.sort()
        if self._binaria_aprobadas(codigo):
            return "Materia Aprobada Por el Alumno"
        else:
            raise Exception("Materia NO Aprobada Por el Alumno")

    def _binaria_aprobadas(self, codigo):
        izq, der = 0, len(self.materias_aprobadas) - 1
        while izq <= der:
            mid = (izq + der) // 2
            if self.materias_aprobadas[mid] == codigo:
                return True
            elif self.materias_aprobadas[mid] < codigo:
                izq = mid + 1
            else:
                der = mid - 1
        return False

    def guardar_aprobadas(self):
        path = os.path.expanduser("~/Documents/archivos/materias.bin")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(self.materias_aprobadas, f)
        print("Materias aprobadas guardadas en archivo.")

    def cargar_aprobadas(self):
        path = os.path.expanduser("~/Documents/archivos/materias.bin")
        if os.path.exists(path):
            with open(path, "rb") as f:
                self.materias_aprobadas = pickle.load(f)
            print("Materias aprobadas cargadas desde archivo:")
            print(self.materias_aprobadas)
        else:
            print("Archivo no encontrado.")

    def agregar_profesor(self, profesor):
        profesor.sig = self.profesores_cursados
        self.profesores_cursados = profesor

    def mostrar_profesores(self):
        print(f"\nProfesores cursados por {self.nombre}:")
        actual = self.profesores_cursados
        while actual:
            print(actual)
            actual = actual.sig

# ============================
# MENÚ INTERACTIVO
# ============================

    def menu():
        alumno = Alumno("Sofía", "Martínez", "12345678", "A100", "Ingeniería", "sofia@unab.edu.ar", "2022-03-10")

        while True:
          print("""
        === Menú ===
        1. Asignar materia
        2. Comenzar próxima materia
        3. Aprobar materia
        4. Mostrar materias pendientes
        5. Eliminar materia
        6. Verificar materia aprobada
        7. Guardar materias aprobadas
        8. Cargar materias aprobadas
        9. Agregar profesor
        10. Mostrar profesores
        0. Salir
        """)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            comision = input("Comisión: ")
            anio = int(input("Año de carrera: "))
            carrera = input("Carrera: ")
            materia = Materia(codigo, nombre, comision, anio, carrera)
            alumno.asignar_materia(materia)
    elif opcion == "2":
            alumno.comenzar_materia()
    elif opcion == "3":
            alumno.aprobar_materia()
            elif opcion == "4":
            alumno.mostrar_materias()
            elif opcion == "5":
            codigo = input("Código de materia a eliminar: ")
            alumno.eliminar_materia(codigo)
            elif opcion == "6":
            codigo = input("Código de materia a verificar: ")
            try:
                print(alumno.verificar_aprobada(codigo))
            except Exception as e:
                print("Excepción:", e)
        elif opcion == "7":
            alumno.guardar_aprobadas()
        elif opcion == "8":
            alumno.cargar_aprobadas()
        elif opcion == "9":
            nombre = input("Nombre profesor: ")
            apellido = input("Apellido: ")
            materia = input("Materia: ")
            anio_ingreso = int(input("Año de ingreso: "))
            profe = Profesor(nombre, apellido, materia, anio_ingreso)
            alumno.agregar_profesor(profe)
        elif opcion == "10":
            alumno.mostrar_profesores()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

    if __name__ == "__main__":
         menu()

    def menu():
       alumno = Alumno("Sofía", "Martínez", "12345678", "A100", "Ingeniería", "sofia@unab.edu.ar", "2022-03-10")

    while True:
        print("""
        === Menú ===
        1. Asignar materia
        2. Comenzar próxima materia
        3. Aprobar materia
        4. Mostrar materias pendientes
        5. Eliminar materia
        6. Verificar materia aprobada
        7. Guardar materias aprobadas
        8. Cargar materias aprobadas
        9. Agregar profesor
        10. Mostrar profesores
        0. Salir
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            comision = input("Comisión: ")
            anio = int(input("Año de carrera: "))
            carrera = input("Carrera: ")
            materia = Materia(codigo, nombre, comision, anio, carrera)
            alumno.asignar_materia(materia)
        elif opcion == "2":
            alumno.comenzar_materia()
        elif opcion == "3":
            alumno.aprobar_materia()
        elif opcion == "4":
            alumno.mostrar_materias()
        elif opcion == "5":
            codigo = input("Código de materia a eliminar: ")
            alumno.eliminar_materia(codigo)
        elif opcion == "6":
            codigo = input("Código de materia a verificar: ")
            try:
                print(alumno.verificar_aprobada(codigo))
            except Exception as e:
                print("Excepción:", e)
        elif opcion == "7":
            alumno.guardar_aprobadas()
        elif opcion == "8":
            alumno.cargar_aprobadas()
        elif opcion == "9":
            nombre = input("Nombre profesor: ")
            apellido = input("Apellido: ")
            materia = input("Materia: ")
            anio_ingreso = int(input("Año de ingreso: "))
            profe = Profesor(nombre, apellido, materia, anio_ingreso)
            alumno.agregar_profesor(profe)
        elif opcion == "10":
            alumno.mostrar_profesores()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()




