
# Juagar a los DADOS 
# Funcion recibe un Numero entre 1 y 6 
# Simula una tirada de DADOS
# Si coincide con el NUMERO recibido devuelve TRUE
# Si no coincide devuelve un FALSE

import random

def tirada_dado (NUMERO: int) -> bool:
    maquina = random . randint (1 , 6)
    return maquina == NUMERO

for i in range (5) :
    usuario = int (input( "Eligeun NUMERO entre 1 y 6 "))
    resultado = tirada_dado (usuario)
    if resultado :
        print ("Ganaste !")

    else :
        print ("Perdiste !")

        print ("------")






