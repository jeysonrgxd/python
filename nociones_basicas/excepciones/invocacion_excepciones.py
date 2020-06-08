# ejecutamos una funcion el cual tiene validacion que si no le pasamos nada de parametros osea algo es None entonses generamos una excepcion y la controlamos con el try except

def mi_funcion(algo=None):
   if algo is None:
      # print("Error... La funcion require parametros")
      # Lazamos una excepcion con la palabra recervada raise , y acontinuacion el nombre del tipo de error con el mensaje
      raise ValueError("Error! No se permite un valor nulo")

# mi_funcion()

# tambien podemos capturar esas excepcion
def mi_funcion2(algo = None):
   try:
      if algo is None:
         raise ValueError("Error! No se permite un valor nulo")
   except:
      print("Error! No se permite un valor nulo")

mi_funcion2()

