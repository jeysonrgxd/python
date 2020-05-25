# Scripts que se ejecutaran en la consola con argumentos para poder automatizar tareas
# importamos la libreria sys que nos dara los argumento que le pasemos ala ejecucion del script en la terminal
import sys

argumentos = sys.argv
print("Los argumento del script son:",argumentos)

if len(argumentos) > 1:
   texto = argumentos[1]
   cantidad = int(argumentos[2])

   for data in range(cantidad):
      print(texto)
else:
   print("\nDigite los parametros nesesarios para poder realizar la operacion")
   print("Ejemplo python scripts.py 'texto', 3")