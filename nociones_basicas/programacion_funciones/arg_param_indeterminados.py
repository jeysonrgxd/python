# Las colecciones listas conjuntos estos datos se envian por referencia y no una copia como los demas tipos, por ende si utilizamos una colleccion dentro de una funcion y la modificamos cambiara tambien en la afuera la funcion osea la global

def doblar_valores(numeros):
   for i,n in enumerate(numeros):
      numeros[i] *=2

ns = [10,50,100]
doblar_valores(ns)
print(ns)

# para que no modifique el valor usamos pequeños trucos
def doblar_numeros(numeros):
   for i,n in enumerate(numeros):
      numeros[i] *=2
   print(numeros)

ns2 = [2,4,6,8]
doblar_numeros(ns2[:])
print(ns2)

