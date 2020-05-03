# Comparacion de cadenas comenzamos con cadenas por que lo demas ya sabemos
print("COMPARACION DE CADENAS\n")
a="hola"
c = "hola" == "hola"
d = a[0] == "h"
print("El resultado de c es",c)
print("El resultado de c es",d)

# comparaciones con listas
print("\nCOMPARACION DE LISTAS\n")

l1 = [1,2,3,4]
l2 = [1,2*2,3*3,4*4]
cl = l1 == l2
cl2 = l1[0] = l2[0]
cl3 = len(l1) == len(l2)
print(cl)
print(cl2)
print(cl3)

# Compraciones de booleanas recordar que aritmeticamente True es == 1 y False ==0
print("\nCOMPARACIONES BOLEANAS \n")

t1 = True == False
t2 = True == True
t3 = True*0 == False
t4 = True>False
t5 = False != True
t6 = False > True
t7 = False * True
t8 = False/5

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)

