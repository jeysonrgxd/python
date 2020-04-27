print("Esto es una \tTabulacion")

# salto de linea y como hacerle saber que deve imprimir el caracter comillas (\"imprime\")
print("\"Esto\" es un \nSalto de linea")

# para que no tome en cuenta los caracteres especiales especificamos que es un crudo poniendole la "r" adelante
print(r"C:\nombre\directorio")

# imprimir multiples lineas
print('''Primera linea
segunda linea
tercera linea\t tabulacion''')

# concatenacion
c1 = "una Cadena"
c2 = "segunda Cadena"
print(c1+c2)
print(c1, c2)

# multiplicion
diez_espacios = " "*10
print(diez_espacios + "un texto a diez espacios")