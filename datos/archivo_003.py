# Pia al usuario un Nombre de la lista
# Indique si esa persosona está en la lista
# Y en dique en que posición en la lista del archivo esta

archivo = open ('Estroctura de datos/ archivo_1 / archivo3.txt')
lista = archivo.readlines()
print (lista)

def buscar_Nombre ():
    nombe_a_buscar = input ('Ingrese el Nombre que quiere buscar:')
    contador = 1
    indice = None
    for a in lista:
        print(f'contador{contador}')
        print (f'indice{indice}')
        print(nombe_a_buscar)
        print (a[0: -1])
        if nombe_a_buscar == a[0: -1]:
         indice = contador
        else :
         contador = contador +1

    if indice == None:
           reuesta = 'Nombre no encontrado'
    else :
           repuesta = f'elNombre esta en la posición{indice}'

    return repuesta
        







        
 