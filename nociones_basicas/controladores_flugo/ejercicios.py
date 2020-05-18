'''
1) Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción válida, el programa informará de que no es correcta.

'''
num1 = int(input("Digita un numero: "))
num2 = int(input("Digita otro numero: "))

opcion = input('''
escoje entre a b y c 
a) Mostrar una suma de los dos números digitados
b) Mostrar una resta de los dos números digitados
c) Mostrar una multiplicación de los dos números digitados
''')

if(opcion == "a"):
   print("La suma de los numero es:",num1+num2)
elif(opcion == "b"):
   print("La resta de los numeros es:",num1-num2)
elif(opcion == "c"):
   print("La multiplicacion de los numeros es:",num1*num2)
else:
   print("La opcion escojida no se encuentra")


'''
2) Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
'''
# Reconociendo el numero par
while True:
   num10 = float(input("Digita un numero: "))
   if(num10%2 == 0):
      print("El numero es par. Adios 😀")
      break
   else:
      print("El numero no es par por favor vuelva a intentarlo para salir del bucle")
      
# reconociendo el numero impar
numero_inpar = 0
while(numero_inpar%2 == 0):
   numero_inpar=float(input("Digite un numero impar: "))