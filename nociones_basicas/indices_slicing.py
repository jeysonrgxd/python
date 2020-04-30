palabra = "python"

'''
| P | Y | T | H | O | N |

------>
| 0 | 1 | 2 | 3 | 4 | 5 |

                        <------
| -6 | -5 | -4 | -3 | -2 | -1 |

'''
print(palabra[0])
print(palabra[1])
print(palabra[2])
print(palabra[3])
print(palabra[4])
print(palabra[5])
print("\n")
print(palabra[-6])
print(palabra[-5])
print(palabra[-4])
print(palabra[-3])
print(palabra[-2])
print(palabra[-1])

# Slicing
print('''\n SLICING ''')

print(palabra[:]) #imprime todo python
print(palabra[1:]) #imprime ython osea de la pocision que especificamos para adelante
print(palabra[:5]) #imprime pytho no toma el ultimo especificado "recordar eso"

print(palabra[:99]) # imprime todo devido que especificamos una pocios que supera a la cantidad normal de la palabra

print(palabra[99:]) # me imprime vacio devido a que le espeificamos una pocios que supera a la cantidad y que supuestamente dessde ahi imprimi por ende nada 

print(palabra[:-2]) # imprime asta donde especificamos menos ese especificado
print(palabra[-2:])# imprime del especifaco asia adelante

'''
En esta parte especificamos la concatenacion o la creacion de otra palabra utilizando la que tenemos
len(palabra) es una funcion que nos dice la cantidad de lementos que conforman la cadena de texto 
'''
concatenacion1 = "T"+palabra[1:len(palabra)]
concatenacion2 = "T"+palabra[1:6]
print(concatenacion1)
print(concatenacion2)