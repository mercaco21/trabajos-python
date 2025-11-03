# Ejercicio : Supongamos que hacemos una "tirada" de 10 dados.
# Ganaremos $200 si la suma de los valores esta entre los 10 y 23.
# Perderemos $1600 si la suma de los valores es 24 o 48.
# Ganaremos $2500 si la suma de los valores es 42.
# # Perderemos $500 en cualquier otro caso.
# Deberiamos jugar a este juego?

#generar una tira de dados
import random

tirada = [random.randint(1,6) for _ in range(10)]
print('Tirada :', tirada)

sum_tirada = sum(tirada)

if 10 <= sum_tirada <=23:
    print('Ganaste 200')
elif 24 <= sum_tirada <=48:
    print('Perdiste 1600')
elif sum_tirada == 42:
    print('Ganaste 2500')
else:
    print('Perdiste 50')           

print(sum_tirada)

