nombre = "Jeyson"
apellido = "Ramos Garcia"

print("Hola {}".format(nombre))

# el nombre es 0 y apellido 1
print("Nombre completo {1} {0}".format(nombre,apellido))

# valor por parametro, ya con esto no importa el orden en cl cual le pasemos los datos al format
print("Nombre completo {n} {a}".format(n=nombre,a=apellido))

# espacios, osea especifico los espacios a la izquierda que tendra antes de poner el nombre
print("{:>30}".format(nombre))

# espacios a la derecha
print("{:30}".format(nombre))

# alineamiento al centro, osea 30 espacios ala derecho y 30 espacios a la izquierda
print("{:^30}".format(nombre))

# truncamiento a 3 caracteres
print("{:.3}".format(nombre))

# trucamiento con 30 espacios a la izquierda
print("{:>30.5}".format(nombre))

# ======= TRABAJANDO CON FORMATEOS DE NUMEROS =======

# formateo de numeros enteros, rellenados con espacios
print("{:4d}".format(1))
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

# formateo de numeros enteros, rellenados con ceros
print("\n{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

# formatep de numeros flotantes, rellenados con espacios
print("\n{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

# formateo de numeros flotantes, rellenados con espacios
print("\n{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))

