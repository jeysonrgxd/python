'''
1) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

'''
try:
   resultado = 10/0  
   print(resultado)
except ZeroDivisionError:
   print("No se puede realizar la division entre 0 por favor divido por otro nuemro")

'''
2) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

'''
try:
   lista = [1, 2, 3, 4, 5]
   print(lista[10])
except IndexError:
   print("Error: No existe dicho indice en el rango")

'''
3) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

'''
try:
   colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
   print(colores['blanco'])
except KeyError:
   print("Error: La clave del diccionario no se encuentra deves probar con otro que si exista")

'''

4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

'''
try:
   resultado = 15 + "20"
   print(resultado)
except TypeError:
   print("No se puede sumar un numero con una cadena de texto y viciversa se deve usar str() y convertir en numero a cadena")

'''
5) Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

'''
def agregar_una_vez(lista,valor):
   try:
      if valor in lista:
         raise ValueError
      else:
         mi_lista = lista
         mi_lista.append(valor)
         print(mi_lista)
   except:
      print("Error: Imposible añadir elementos duplicados =>",lista)

elementos = [1, 5, -2] 
agregar_una_vez(elementos[:],-2)
print(elementos)

   

   