# conversiones
n = int("10")

f = float("10.5")

c = "Un texto y un numero "+str(10) + " " + str(3.14)

print(n,"\n",f,'\n',c,)

print("numero 10 en binario:",bin(10))
print("numero 12 en exadecimal:",hex(12))

print("el numero binario 0b1010 a entero es" ,int(0b1010))
print("el numero exadecimal 0xc a entero es" ,int(0xc))

# funcion str(#) que acepta un numero y sirve para concatenar texto con numeros
tu_edad = "mi edad es: " + str(25)
print(tu_edad)
print(type(str(1000))) #esto no compruba que transforma a estring 

# eval funcion que podemos meter variables en texto como el echo en php
nombre_completo = "jeyson gino ramos garcia"
print("mi nombre es:",eval("nombre_completo"))
num1 = 10
num2 = 10
print("los numero {} y {}".format(num1,num2),"al multiplicar dan:",eval("num1*num2"))