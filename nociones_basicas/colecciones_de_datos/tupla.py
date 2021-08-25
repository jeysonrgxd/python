# La tuplas son listas inmutables y se diferencia en que las lista son con [] y las tuplas con parentesis tupla()
tupla = (1,"Jeyson",[2,3,4],False,1)
print(tupla)

# podemos usar algunos metodos de las listas tambien en la tupla
print("Longitud de la tupla:",len(tupla)) #cantidad de elementos en la tupla
print("Posicicion del nombre jeyson en la tupla:",tupla.index("Jeyson")) #buscar posicion de la palabra

# podemos usar slicing
print(tupla[2::])

#cuantos repetidos hay en la tupla
print("El numero 1 se repite",tupla.count(1)) 

# No se puede usar tupla.append() ya que las tuplas son inmutables

# convirtiendo una tupla a lista
nombres = ("jeyson","andersson", "estefany")
lista_nombres = list(nombres)
print(lista_nombres)

# convirtiendo una lista en tupla
numeros = [1,2,3,4,5]
tuplaNumero = tuple(numeros)
print(tuplaNumero)