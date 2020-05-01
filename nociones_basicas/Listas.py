# Adiferencia de las cadena de caracteres las listas no son inmutables por ende podemos modificar su contenido

# no tenemos restriccion en los tipos que tenemos dentro de una lista
numeros = [1,2,3,4,5]
datos = [4,"Una cadena", -15,3.14,"otra cadena"]
concatenacion = numeros + [6,7,8,9,10]
pares = [0,2,4,5,8,10]
pares[3] = 6
pares.append(12)
pares.append(7*2)
letras = ['a','b','c','d','e','f']
letras[:3] = ['A','B','C'] #cabiando contenido con slicing
letras[-3:] = [] #borramos el contenido ['d,'e','f']
letras = [] # borramos todo igualando a una lita vacia

# Capicidad de tener listas en otras listas (Listas anidadas)
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
r=[a,b,c] #ponemos en r las demas listas a b c

print(datos[0])
print(datos[-1])
print(datos[-2:]) #slicing
print(concatenacion) #concatenacion de lista
print(pares) # podemos remplazar un contenido
print(letras)
print(len(pares)) #imprime la longitud de la lista pares
print(r)
print(r[0])
print(r[-1])
print(r[0][1])
print(r[1][2])
print(r[-1][-1]) #una forma de acceder al ultimo elemento de una lista y al ultimo de elemento del seleccionado

