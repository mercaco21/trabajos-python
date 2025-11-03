
def metros_a_mm (metros : float = 0.0 ) -> float:
    return metros * 1000

def pulgadas_a_mm (pulgadas : float = 0.0) -> float:
    return  pulgadas * 25.4

print (metros_a_mm (float(input ("ingrese una longitud en metros : "))))
print (pulgadas_a_mm (float(input("ingrese una longitud en pulgadas:"))))

    

