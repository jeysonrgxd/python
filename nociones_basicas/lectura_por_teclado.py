#esto esperara que escribamos valores por consola
valor=input("Escribe un texto o numero lo que sea ")
print("El valor que pusistes es "+valor)
print("El valor que pusistes es {}".format(valor))
print("El valor que pusistes es",valor) 

numeroText = input("Escribe un numero que sera transformado a entero: ")
numeroInt = int(numeroText)
print("lo convertimos a un numero entero {}".format(numeroInt))

numeroText2 = input("Escribe un numero decimal que sera transformado a float:")
numeroFloat = float(numeroText2)
print("lo convertimos a un numero entero flotante",numeroFloat)

# forma rapida de convertir la entrada de teclado a numero
numeroFazt = int(input("Digita un numero entre 100 - 500 "))
numeroFazt +=10
print("El numero digitado se le sumo 10 y resulto ",numeroFazt) 

