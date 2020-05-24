# Importamos una libreria de python para hacer las colas
from collections import deque

print("\n---------PILAS---------")

# Las pilas el ultimo en entrar es el primero en salir
numeros = [1,2,3,4,5]
numeros.append(6)
numeros.append(7)
numeros.append(8)

print("La pila es:",numeros)

primero_salir = numeros.pop()
penultimo_salir = numeros.pop()

print("Salieron dos de la pila los cuales son:",primero_salir,"y",penultimo_salir)
print("Ahora solo quedan en la pila {}".format(numeros))

'''
Las colas el primero en entrar es el primero en salir
- utilizado es mayormente en servidores para obtener peticiones que se le hacen y ponerlos en la cola para atenderlo de acuerdo al orden de llegada

'''
print("\n------COLAS------")
cola = deque()
print("Esto es una cola",cola)

# ponemos una lista en la cola
cola2 = deque(numeros)
print("Ahora si la cola esta llena",cola2)

# tambien podemos usar el append en las colas para agregar uno mas
cola2.append(7)
print(cola2)

# sacamos al primero que entro
primero_decola = cola2.popleft()
print("El primero de la cola en salir y tambien es el que entro primero es:",primero_decola)
