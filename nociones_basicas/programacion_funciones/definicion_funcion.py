# DEFINICION DE FUNCIONES

def saludar():
   print("Hola")

saludar()

nombre = "jeyson"

def di_nombre():
   # al definir global a la variable que utiliaremos si cambia su valor, pero si no la utilizamos python crea otra variable en el ambito de la funcion no importa que tengo el mismo nombre pero son distintas variables
   # global nombre
   nombre = "ramos"
   print(nombre)

di_nombre()
print(nombre)