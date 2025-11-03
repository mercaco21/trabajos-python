
# Convertir las temperaturas de Celsius {celsius:.2f}°C
# Convertir las temperaturas de Fahrenheit {fahrenheit:.2f}°f
# Anotar en el escritori los grados fahhrenheit son un float y tambien los grados celcius.

# Las formulas de conversión son 

# fahrenheit = celsius x (9 / 5) + 32 
# celsius = (fahrenheit - 32) x (5 / 9)

# Convertir las temperaturas de Celsius

#(def convertir_temperaturas(): # Llamar a la función
    
    # Convertir de Celsius a Fahrenheit
 #   celsius = float(input("Ingrese temperatura en Celsius: "))
 #   fahrenheit = celsius * (9 / 5) + 32
 #   return(f"{celsius}°C = {fahrenheit:.2f}°F")
    
    # Convertir de Fahrenheit a Celsius
#    fahrenheit = float(input("Ingrese temperatura en Fahrenheit: "))
#    celsius = (fahrenheit - 32) * (5 / 9)
#    return(f"{fahrenheit}°F = {celsius:.2f}°C")  )


# Llamar a la función  - (todo LOL QUE ESTA AHORA marcado con asterisco es la formula echa
# co DEPEpSEEE la IA  
#convertir_temperaturas()
# En este ejercicio esta llamada la funcion con los dos cambios de tenperatura en la definición def que estan 
# Las dos temperaturas identadas 

# Puntos Importantes
# Usar floats: Como mencionaste, ambas temperaturas deben ser float para mayor precisión

# Orden de operaciones: Python sigue el orden matemático normal (multiplicación/división antes que suma/resta)

# Precisión: Puedes formatear la salida con :.2f para mostrar 2 decimales todo LOL QUE ESTA AHORA marcado con asterisco es la formula echa
# co DEPEpSEEE la IA  

# trabajo necho por Mario amigo de DIEGO 

def convertir_celsius (celsius : float) : 
    grados = celsius * (9 / 5) + 32
    return grados

def convertir_fara (fara : float):
    fara = (fara - 32) * (5 / 9)
    return fara

print(convertir_celsius (18))
print (convertir_fara (64.4))
 



