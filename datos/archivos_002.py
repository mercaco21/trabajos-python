# Lee una sola linea , Hasta el salto ('\n')

archivo_a_leer = open ('./datos/archivo3.txt','r')
print (archivo_a_leer.readline())

archivo_a_leer.close()

# Archivo a leer todos los contenidos del mismo

archivo_a_leer = open ('./datos/archivo3.txt','r')
print (archivo_a_leer.read())

archivo_a_leer.close()

# Lee todos los contenidos de una lista 

archivo_a_leer = open ('./datos/archivo3.txt','r')
print (archivo_a_leer.readlines())

archivo_a_leer.close()

