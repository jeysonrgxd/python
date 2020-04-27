# python no tiene constantes (no existe)
# python no tiene tipos de datos
a = '10'
b = 10.2 # variable flotante

# recordar que para otorgar a una variable un valor boolean se de ve poner la primero letra en mayuscula
x = True
y = False

print(b) 
# se le quita los decimales al convertirlo en entero
print("casteamos el flotante a entero ", int(b)) 

# type hinting
def sumar(x:int, d:int):
   print(x + d)

sumar(3,5)