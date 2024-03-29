# Los diccionarios son como los objetos de javascript, o tambien conocidos en otros lenguajes como arreglos asociativos, tiene clave y valor
persona1 = {
   "nombre":"Jeyson",
   "apellido":"Ramos Garcia",
   "edad":23
}
print(persona1["nombre"])

# Tambien podemos modificar los datos del diccionario
persona1["nombre"] = "Jeyson gino"
persona1["edad"] +=2

#Recoremos el diccionario
print("\nImprimiendo el valor de las claves mediante un for")
for clave in persona1:
   print(persona1[clave])

#Recoremos solo las claves diccionario
print("\nImprimiendo el solo las claves mediante un for")
for clave in persona1.keys():
   print(clave)

#Recoremos solo los valores diccionario
print("\nImprimiendo solo el valor en un for")
for valor in persona1.values():
   print(valor)

# utiizando el items de los diccionarios
print("\nImprimiendo clave y valor mediante items()")
for clave,valor in persona1.items():
   print(clave,"=>",valor)

#Uniendo listas con diccionarios el famoso listas de diccionarios o tambien conocido en otros lenguajes el array de objetos
lista_persona = []
persona2 = {
   "nombre":"Andersson",
   "apellido":"Caceres Garcia",
   "edad":25
}
persona3 = {
   "nombre":"Steven",
   "apellido":"Guevara Garcia",
   "edad":11
}

lista_persona.append(persona1)
lista_persona.append(persona2)
lista_persona.append(persona3)
print("Imprimimos la lista de diccionarios que almacenamos",lista_persona)
print("Mostramos los datos mediante un for")

for persona in  lista_persona:
   print(persona["nombre"],persona["apellido"],persona["edad"])

