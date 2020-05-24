'''
1) Realiza un programa que siga las siguientes instrucciones:

Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
Crea un conjunto llamado administradores con los administradores Juan y Marta.
Borra al administrador Juan del conjunto de administradores.
Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
Notas: Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista. También cuentan con un método llamado .discard(elemento) que sirve para borrar un elemento.
'''

usuarios = {"Marta","David","Elvira","Juan","Marcos"}
administradores = {"Juan","Marta"}
# administradores.remove("Juan") se puede hacer de esta forma tambien pero esto lanza una excepcion si no encuentra el valor a comparacion de discar que si no encuentra solo le deja pasar osea lo ignora
administradores.discard("Juan")
# agregamos a marcos en el conjunto de administradores
administradores.add("Marcos")

print("------------- EJERCICIO 1 -------------")

for user in usuarios:
   if(user in administradores):
      print("El usuario",user,"es administrador")
   else:
      print("El usuario",user,"no es administrador")

'''
2) Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.
El guerrero tiene el doble de ataque y alcance que un caballero.
El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
Muestra como quedan las propiedades de los tres personajes.

'''

print("------------- EJERCICIO 2 -------------")
vida = 2
defensa = 2
ataque = 2
alcance = 2

personajes = [
   {
      "nombre":"caballero",
      "vida":vida*2,
      "defensa":defensa*2,
      "ataque":ataque,
      "alcance":alcance
   },
   {
      "nombre":"guerrero",
      "vida":vida,
      "defensa":defensa,
      "ataque":ataque*2,
      "alcance":alcance*2
   },
   {
      "nombre":"arquero",
      "vida" : vida,
      "ataque":ataque,
      "defensa":int(defensa/2),
      "alcance":alcance*4

   }
]

for i,personaje in enumerate(personajes):
   print("\nPersonaje",i+1)
   for clave,valor in personaje.items():
      print(clave,"=>",valor)