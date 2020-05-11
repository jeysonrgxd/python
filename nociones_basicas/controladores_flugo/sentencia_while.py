# ===========while simple ===========
# c=0
# d=0
# while c<=5:
#    c +=1
#    print("El valor de c es",c)


# ===========usando por default else===========
# d=0
# while d >= 1:
#    c +=1
#    print("c vale",c)
# else:
#    print("Se ha completado toda la iteraciòn y d vale",d)

#=========== break romper el flujo ===========
# a=0
# while a<=10:
#    a +=1
#    if(a == 5):
#       print("El resultado de a es {} adios".format(a))
#       break
#    print("El valor de a es",a)

#=========== saltar el flujo ===========
# f= 0
# while f<=10:
#    f +=1
#    if(f==7):
      # print("el valor de f es {} entonses continuamos ala otra iteracion sin realizar lo de abajo".format(f))
   #    continue
   # print("el valor de f es",f)

# ============ ejercicio menu consola ============
while True:
   print("""¿Qué quieres hacer? Escribe una opcion
   1) Saludar
   2) Sumar dos números
   3) Salir""")
   opcion  = input()
   
   if opcion == '1':
      print("Hola jeyson como vas com el curso")
   
   elif opcion == '2':
      num1 = float(input("Digita el primer numero: "))
      num2 = float(input("Digita el segundo numero: "))
      print("La suma de los numero digitados es",num1+num2)
   
   elif opcion == '3':
      print("Hasta luego jeyson anda duerme ya")
      break
   
   else:
      print("Comando desconocido, vuelve a intentarlo")
