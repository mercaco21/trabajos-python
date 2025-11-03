# Enlaces para hoy 
# https://docs.python.org/es/3.14/library/os.html# 
# https://docs.python.org/es/3.14/tutorial/inputoutput.html
# https://www.freecodecamp.org/espanol/news/tutorial-de-f-strings-en-python-formato-de-cadenas-en-python-explicado-con-ejemplos/
# keep
# Fijado

# Escritura de archivo de texto.
archivo = open ('./datos/archivo1.txt','w')
archivo.write ('linea1\n')
archivo.write ('linea2\n')
archivo.write ('linea3\n')
archivo.close()

# agregar contenidos al final de un archivo existnte

archivo = open ('./datos/archivo1.txt', 'a')
archivo.write ('Nueva linea agregad\n')



