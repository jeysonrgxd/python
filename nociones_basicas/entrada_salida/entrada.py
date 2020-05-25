# Entradas de datos atravez la consola

veses = int(input("Digita un numero: "))
numeros= []

for i in range(veses):
   numeros.append(int(input("escribe un numero: ")))

print("La lista de numeros es:",numeros,"Y la suma de los numeros es:",sum(numeros))