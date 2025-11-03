#codigo para clase auto


class Vehiculo:
    def __init__ (self,color, cant_ruedas, cant_puertas, modelo, marca, dimensiones, velocidad = 0):
        self.color = color
        self.cant_ruedas =cant_ruedas
        self.cant_puertas =cant_puertas
        self.modelo =modelo
        self.marca =marca
        self.dimensiones =dimensiones
        self.velocidad = velocidad

    def Acelerar(self):
        self.velocidad = self.velocidad+20

    def Frenar(self):
        self.velocidad = self.velocidad-20

auto_de_mario = Vehiculo('rojo',4,2,'deportivo','ferrari','largo')


print(auto_de_mario.velocidad)

print(auto_de_mario.Acelerar())

print(auto_de_mario.velocidad)

print(auto_de_mario.Acelerar())

print(auto_de_mario.velocidad)

print(auto_de_mario.Frenar())

print(auto_de_mario.velocidad)

print(auto_de_mario.Frenar())

print(auto_de_mario.velocidad)







#codigo generador de cuil para personas


#import random

#class Persona:
 #   def __init__ (self, apellido, nombre, fecha_nacimiento, dni, genero):
      #  self.apellido = apellido
      #  self.nombre = nombre
      #  self.fecha_nacimiento = fecha_nacimiento
      #   self.dni = dni
      #   self.genero = genero.upper()

   # def Genera_cuil(self):
    #   primeros_numeros = 0
    #   ultimo_numero = 0
    #  if self.genero.upper() == 'M':
        # primeros_numeros = 20
    # if self.genero.upper() == 'F':
        #  primeros_numeros = 27
    # if self.genero.upper() == 'N':
        #  primeros_numeros = 30
   
    #  ultimo_numero = random.randint(0, 9)
   
    #  return f"{primeros_numeros}-{self.dni}-{ultimo_numero}"
   



#persona1 = Persona('Juarez','Julio','1935','11554488','M')
#print(persona1.apellido)

#print(persona1.Genera_cuil())
