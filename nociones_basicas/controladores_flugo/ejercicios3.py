'''
5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

'''

numeros = [0,1,2,3,4,5,6,7,8,9]
num = 10
while (num in numeros) != True: 
   num =  int(input("Digita un numero que este entre 0 y 9: "))
else:
   print("El numero se encuentra en esta lista ",numeros)

'''
6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 0, 1, 2, ..., 10
Todos los números del -10 al 0 -10, -9, -8, ..., 0
Todos los números pares del 0 al 20 0, 2, 4, ..., 20
Todos los números impares entre -20 y 0 -19, -17, -15, ..., -1
Todos los números múltiples de 5 del 0 al 50 0, 5, 10, ..., 50
Pista: Utiliza el tercer parámetro de la función range(inicio, fin, salto).

'''

print(list(range(0,11)))
print(list(range(-10,1)))
print(list(range(0,21,2)))
print(list(range(-19,0,2)))
print(list(range(0,51,5)))

'''
7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:

'''
print("\n Ejercicio 7")
lista_1 = ["h","o","l","a"," ","m","u","n","d","o"]
lista_2 = ["h","o","l","a"," ","l","u","n","a"]
lista_3 = []
lista_4 = [lista_1,lista_2]

for a in lista_1:
   for b in lista_2:
      if a == b:
         if(lista_3.count(a)<1):
            lista_3.append(a)

print(lista_3)

print("\nSegundo metodo para resolver el problema usando las operadores logicos")
for lista in lista_1:
   # if (lista in lista_2) and (lista in lista_3 == False):
   #reducimos codigo usando not tambien puede ir asi para que sea mas legible (list not in lista_3)
   if (lista in lista_2) and (not lista in lista_3): 
      lista_3.append(lista)

print(lista_3)



