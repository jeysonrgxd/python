def obtener_nombre():
   return 'Jeyson gino ramos'

mi_nombre = obtener_nombre()

print(mi_nombre)

# me devuelve una lista de diez numeros pero al impirmir tenemos que pasar por la funcion list()
def diesnumeros():
   return range(10)

print(list(diesnumeros()))

# destructuring parecido a javascript
def valoresjs():
   return 'jeysonRG', 25, 'programar'

nombre,edad,hobbi = valoresjs()
print("esto devuelve la funcion al hacer ese return:",valoresjs(),'es una tupla')
print('estos son los valores al pasarle alas variables',nombre,edad,hobbi)