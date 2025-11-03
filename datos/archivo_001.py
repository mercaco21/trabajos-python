# Escritura de archivo de texto

archivo = open ('./datos/archivo1.txt ','w')
archivo.write ('linea1\n')
archivo.write ('linea2\n')
archivo.write ('linea2\n')

archivo.close()

# Agregar contenido al final de una Fila al archivo existente

archivo1 = open ('./datos/archivo1.txt ','a')
archivo1.write (' Nueva linea agregada\n')

archivo1.close()

# Escribir un archivo que no existe.

archivo2 = open ('./datos/archivo2.txt ','w')
archivo2.write ('archivo2.linea1\n')
archivo2.write ('archivo2.linea2\n')

archivo2.close()

# Agregar un archivo que no exixste ( se crea )

archivo3 = open ('./datos/archivo3.txt ','a')
archivo3.write ('archivo3.linea1\n')
archivo3.write ('archivo3.linea2\n')

archivo3.close()