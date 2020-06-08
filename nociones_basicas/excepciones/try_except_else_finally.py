# Utilizaremos try except else finally
'''
try: busca si hay algun error
except: que ara si hay error
else: si no hay error hacer algo
finally: asi hay o no hay error ara algo

'''

while True:
   try:
      numero =  float(input("Digita un numero: "))
      print("El numero es {} lo dividimos entre 4 y nos da : {}".format(numero,numero/4))
   
   except:
      print("Error por favor vuelva a digitar un numero")
   
   else:
      print("Todo a funcionado correctamente")
      break #Importante romperla iteracion si todo ha salido bien
   
   finally:
      print("Fin de la iteracion")