#  OPERADOR not
#  not true = false

# dos formas de expresion logicas por conjuncio(AND) y disyuncion(OR)
'''
>> True and True
True
>> not True
False
>> True or False
True
>> False or False
False
>> not True == False
True
>> False and False
False

'''

print("CONJUNCION and\n")
a=13
b = a > 10 and a < 20
print(b) #salida -> True

c = "Hola Mundo"
d = len(c) >= 5 and c[0] == "H"
print(d)

print("\nDISYUNCION or\n")
e = "SALIDA"
f = (e == "EXIT") or (e == "FIN") or (e == "SALIDA")
print(f)

g = "Lector"
i = g[0] == "H" or g[0] == "h"
print(i)