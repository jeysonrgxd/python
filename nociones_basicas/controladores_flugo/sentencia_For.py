# METODO CON EL WHILE DE IMPRIMIR UNA LISTA 
numeros = [1,2,3,4,5,6,7,8,9,10]
# indice = 0
# while indice < len(numeros):
#    print(numeros[indice])
#    indice +=1

# FORMA DE FOR tradicional
print("\nFORMA DEL FOR")
# for numero in numeros:
#    print(numero)

# modificar elementos del array tenemos que agregarle un contador en el mismo for y utilizar "enumarate" que mas omenos no estoy eguro investigar luego, convierte una lista en un objeto iterable la cual nesesitamos si utilizamos un contador en el for funcion de python

# for i,numero in enumerate(numeros):
#    numeros[i] = numero*numero

# print(numeros)

# tambien podemos recorrer una cadena, no podemos usar enumerate ya que no nos serviria ya que una cadena es inmutable, pero podemos crear una nueva cadena y concatenar esa cadena nueva con lo valores que queramos
saludo = "Hola como estas"
cadena_saludo = []

# for caracter in "hola como estas":
for caracter in saludo:
   # imprimimos los caracteres
   print(caracter)
   # creamos una lista con los caracteres
   cadena_saludo.append(caracter)

print(cadena_saludo)
   
# FOR tradicional de los demas lenguajes con rango de numero, recordar que el range(10) comienza de cero asta el numero que le pongamos pero no toma ese ultimo valor sino uno antes de llegar al especificado.

# esta forma de for con una lista creada de 10 numero si queremos queremos iterar de esta forma, opcupa espacio en memoria por eso no es recomendable, a cabio range(10) es interpretado por python , y mas no ocupa espacio en memoria

# for num in [0,1,2,3,4,5,6,7,8,9,10]
for num in range(10):
   print(num)
