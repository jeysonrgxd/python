try:
   numero = float(input("Digita un numero: "))
   # divicion = "wsd"/numero  esto es para probar el TypeError
   divicion = 10/numero
   print(divicion)

except TypeError:
   print("No se puede dividie el numero entre una cadena o viceversa")   

except ZeroDivisionError:
   print("No se puede dividir un numero entre cero")

except ValueError:
   print("Error... Por favor digite un numero")

#con esta forma sabemos cual es nombre de la exepcion, para despues ponerlas validarlas por tipo
except Exception as e:
   print(type(e).__name__)
