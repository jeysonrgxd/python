'''
CONJUNTO : SON COLECCIONES DESORDENADAS  ELEMENTOS UNICOS SE UTILIZAN PARA SER PRUEBAS DE PERTENECIA A GRUPOS, SOPORTAN OPERACIONES MATEMATICAS AVANZADAS

- los conjuntos son desordenados
- set() crea un conjunto vacio asta que le pasemos un valor entre llaves set({1,2,3,4,5})
'''
# conjunto = {1,2,3,4,5}
conjunto = set({1,2,3,4,5})
conjunto.add(6)
conjunto.add(0)
conjunto.add("H")
conjunto.add("A")
conjunto.add("Z")

# como ve lo ordenada de una manera sin cumplir un orden establecido por eso son colecciones desordenadas
print(conjunto)

#los comjunto tambien sirve para comprobar si estan en grupo
grupo = {"jeyson","andersson","steffany"}
print("El nombre jeyson se encuentra en el grupo?","jeyson" in grupo)
print("El nombre maria se encuentra en el grupo?","maria" in grupo)

# en los conjuntos no puede ver datos repetidos
test = {"PYTHON","PYTHON","PYTHON","PYTHON","PYTHON"}
print("Solo hay un elemento en conjunto ya que no puede ser repetido su valor",test)

# transformamos una lista a conjunto para poder quitar los datos repetidos y luego lo volvemos a lista
lista = [1,2,3,3,2,1]
con = set(lista)
lista_sin_repetir = list(con)
print("La lista es",lista,"y agregado a un conjunto y transformado a lista nuevamente",lista_sin_repetir)

# sacamos los datos repetidos de una manera rrapida
nombres_sin_repetir = list(set(["python","javascript","php","java","python"]))
print("lista sin repetir elementos", nombres_sin_repetir)

# tambien podemos usarlo en textos y quitar las laetras repetidas y tam obvio transformalo a lista
palabra = "Al pan pan y al vino vino"
lista_sin_repeticion = list(set(palabra))
print("La plabra o string sin repetir caracteres", lista_sin_repeticion)

# convertir lista sin repeticion a cadena
palabra_sin_repeticion = ''.join(lista_sin_repeticion)
print(palabra_sin_repeticion)

