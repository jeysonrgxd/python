# especificamos el envio de parametros especificando el valor y no importa el orden en el cual enviamos si pasamos de esta forma
def suma(a,b):
   return a-b

print(suma(b=1,a=3))

#argumentos de funcion por defecto, como se observa imprimimos invocando la funcion al cual no le pasamos parametros pero como le agregamos por defecto se raliza
def restar(a=0,b=0):
   return a-b

print(restar())

#valor "None"
def multiplicar(a=None, b=None):

   if(a == None or b== None):
      print("Tiene que enviar parametros ala funcion")
      return

   return a*b

print(multiplicar(3,4))
