'''
1) Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero

'''

# num1 = input("Digite el primer numero ")
# num2 = input("Digite el segundo numero ")

# resp1 = num1 == num2
# resp2 = num1 != num2
# resp3 = num1 > num2
# resp4 = num2 >= num1

# print("Los numeros digitado son iguales",resp1)
# print("Los numeros digitado son diferentes {}".format(resp2))
# print("De los numeros digitados el primero es mayor que el segundo",resp3)
# print("De los numero digitados el segundo es mayor igual que el primero {}".format(resp4))


'''
2) Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiene con mostrar True o False):

'''

# cadena = input("Digite una palabra ")
# resp = (len(cadena)>=3) and (len(cadena)<10)
# print(resp)
# print("Tiene la cadena una longitud mayor o igual que 3 y a su vez es menor que 10 ?",(len(cadena)>=3) and (len(cadena)<10))


'''
3) Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que sea un número entero)
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla

'''

numero_magico = 12345679
numero_usuario = int(input("Digite un numero entre 1 y 9 "))
numero_usuario *= 9
numero_magico *=numero_usuario
print(numero_magico)