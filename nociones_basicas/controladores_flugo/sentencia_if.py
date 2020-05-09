dataA = int(input("Digita un numero: "))
dataB = int(input("Digita otro un numero: "))

# se puede obviarr los parentesis pero no es recomendable ya que los parentesis no ayuda a encerrar las expresiones logicas

# Ojo el flujo de codigo dentro de los if else elfi(ver el otro fichero para entender mejor el elfi) tiene que estar al linea todas las lineas # de codigo sino no funcionara
if (dataA > dataB) and (True):
   print("El numero",dataA,"es mayor que",dataB)

elif(dataA == dataB) or (True):
   print("Los numero digitados son iguales")

else:
   print("El numero",dataB,"es mayor que",dataA)



