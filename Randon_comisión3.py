import random
 

# for i in range(20):
    #randint hace random en numeros enteros
#print(random.randint(1,100))
    # tambien tiene choice para elegir entre opciones
#print(random.choice(['m','a','r','i','o']))

dado_usuario = int(input('¿que valor va a salir?'))
dado_real = random.randint(1,6)


if dado_usuario == dado_real:
    print(dado_real)
    print('Acertaste!')
else:
    print(dado_real)
    print('Perdiste!')

