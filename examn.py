class libro:

     def _init_(self,titulo,autor,num_paginas,anio_publicado):
       self.titulo = titulo
       self.autor = autor
       self.num_paginas = num_paginas
       self.anio_publicado = anio_publicado
       self.prestado = False
       self.num_alumno = ""

    
     def mostrar_informacion(self):
        print(f"titulo: {'titulo'}")
        print(f"autor: {'autor'}")
        print(f"numero paginas: {'num_paginas'}")
        print(f"año de publicación: {'anio_publicado'}")
        print(f"prestado : { 'si' if self.prestado else 'no'}")
     def  prestado (self):
         if not self.prestado :
            self.prestado = True
            print(f"libro '{self.titulo}' presatdo con exito.")

         else: 
          print(f"libro'{self.titulo}' ya esta prestado.") 

     def devulucion (self):
         if self.prestado :
            self.prestado = False
            print(f"libro '{self.titulo}' devolucion con exito.")
         else :
          print(f"libro{self.titulo}' no esta prestado.")
