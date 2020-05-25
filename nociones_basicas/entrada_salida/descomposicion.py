'''
3) Avanzado Crea un script llamado descomposicion.py que realice las siguientes tareas:

Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:

> 3647
El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:

> 0007
  0040
  0600
  3000
Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa

'''
import sys
argumentos = sys.argv

# valida tambien que sea un numero menor que 9999
if len(argumentos)>=2:
   for indice,num in enumerate(argumentos[1][::-1]):
      nultiplicador = "1"+("0"*indice)
      new_num = int(num)*int(nultiplicador)
      print("{:04d}".format(new_num))
else:
   print("Error no se encuentra el argumento nesesario")
   print("Ejemplo: python descomposicion.py 2233")