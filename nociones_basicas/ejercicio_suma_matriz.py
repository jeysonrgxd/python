'''
La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila, el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista ¡Pruébalo!

'''

matriz = [ 
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

matriz[0][-1]=sum(matriz[0][:-1])
matriz[1][len(matriz[1])-1]=sum(matriz[1][:3])
matriz[2][3]=sum(matriz[2][0:3])
matriz[3][len(matriz[1])-1]=sum(matriz[3][0:-1])

print(matriz)