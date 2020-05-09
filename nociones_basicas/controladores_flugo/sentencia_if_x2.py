# Sentencia if

n = 10
if n%2 == 0:
   print("el numero es par")
else:
   print("El numero es impar")


# recordar que solo se ejecuta uno bloque deacierdo ala condicion asi la nota sea 10 y que tu creas que deve pasar por nota>=9, nota>=7 nota>=5, ps no al ser elif de arriva asi abajo el primero que cumple ingresa ejecuta y termina los demas flujos
nota = float(input("Ingresa tu nota de examen de hoy "))
if nota>=9:
   print("Excelente")

elif nota>=7:
   print("Muy Bueno")

elif nota>=5:
   print("Bueno")

else:
   print("Deves estudiar mas")


# donde si se ejecuta varias veses
print("\nsin elif\n")
if nota>=9:
   print("Excelente")

# if nota>=7:
if nota>=7 and nota<9:
   print("Muy Bueno")

# if nota>=5:
if nota>=5 and nota<7:
   print("Bueno")

# else:
#    print("Deves estudiar mas")

# pass define bloques vacios
if True:
   pass
