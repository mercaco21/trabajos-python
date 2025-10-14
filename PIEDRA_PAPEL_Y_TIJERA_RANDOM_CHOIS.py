
# Ejemplo  RANDOM.CHOICE
import random


def jugar_piedra_papel_tijera (eleccion_usuario : str) -> str :
    eleccion_maquina = random.choice (['PIEDRA','PAPEL','TIJERA'])

    if (eleccion_usuario == eleccion_maquina) :
        return 'EMPATE'
    
    if (
        (eleccion_usuario == 'TIJETA' and eleccion_maquina == 'PIEDRA') or
        (eleccion_usuario == 'PAPEL' and eleccion_maquina == 'TIJERA') or
        (eleccion_usuario == 'PIEDRA' and eleccion_maquina == 'PAPEL')
    ) :
        return 'PERDISTE'
    
    if (
        (eleccion_usuario == 'TIJETA' and eleccion_maquina == 'PAPEL') or
        (eleccion_usuario == 'PAPEL' and eleccion_maquina == 'PIEDRA') or
        (eleccion_usuario == 'PIEDRA' and eleccion_maquina == 'TIJERA')
    ) :
        return 'GANASTE'

    return None

for i in range(10):
    eleccion_usuario = str(input('Elige una opcion: piedra, papel o tijera: '))

    resultado = jugar_piedra_papel_tijera(eleccion_usuario)

    print(resultado)