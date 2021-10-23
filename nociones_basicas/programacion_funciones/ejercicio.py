'''
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

Por ejemplo:

pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]
Nota: Para ordenar una lista automáticamente puedes usar el método .sort().

'''

def separar(args):
   pares = []
   impares = []
   for arg in args:
      if arg%2 != 0:
         impares.append(arg)
      else:
         pares.append(arg)
   pares.sort()
   impares.sort()
   print(pares,'\n',impares) 

separar([2,5,10,22,30,37,9,100,97])