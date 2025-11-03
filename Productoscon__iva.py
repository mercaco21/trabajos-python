#   Productos con iva

def calcular__precio(valor: float,iva: float=0.21, descuento: float= 0.0, iibb= 0.0)-> float:
 return valor * (1- descuento) * (1 + iva) * (1 + iibb)


producto1 = calcular__precio (1000)
producto2 = calcular__precio (100, 0.105)
producto3 = calcular__precio (100, 0.075)
# producto4 = calcular__preciio (1000, 0.21, 0.20)
producto4 = calcular__precio (1000, descuento = 0.20)
producto5 = calcular__precio (100, iibb = 0.03)


print (producto1)
print (producto2)
print (producto3)
print (producto4)
print (producto5)


