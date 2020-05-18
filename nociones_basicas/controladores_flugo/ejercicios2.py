'''
3) Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:

Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.

'''
# NOTA si queremos imprimir un range(1,100) con print recordar que esto interpretado asi que debemos comvertirlo en una lista con la funcion list(range(1,100))
print("MOSTRANDO UNA LISTA CON RANGE DE LOS 100 PRIMEROS NUMEROS\n")
print(list(range(0,101))) #mostramos los numero del 0 asta el 100

#el tercerparametro de range es un salta cada cuanto numero asemos el salta y para los pares vasta con dos saltos pero en rango tiene que ser de 0 a 101
print("MOSTRANDO LA SUMA DE LOS NUMERO PARES DEL 0  ASTA 100\n") 
print(sum(range(0,101,2))) 

print("MOSTRANDO LOS NUMEROS PARES DE FORMA TRADICIONAL\n")
numeros_pares = []
for i in range(1,101):
   if i%2 == 0:
      # suma_pares +=i
      numeros_pares.append(i)
print(numeros_pares)
print("La suma de ese array de numeros pares es:",sum(numeros_pares))

'''
4) Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:

'''
cant = int(input("Cuantos numeros desea introducir: "))
numeros = []
for num in range(cant):
   inp = float(input("Escriba un numero: "))
   numeros.append(inp)
print("La media de los numeros ingresado es", sum(numeros)/len(numeros))
