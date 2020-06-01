# ARGUMENTOS Y PARAMETROS INDETERMINADOS

# ARGUMENTOS INDETERMINADOS (un * es una tupla)

def getNumbers(*args):
   return args

print('Un * retorna una tupa',getNumbers(1,2,3,4,5,7,8),'\n')

def sumatoria(*args):
   suma = 0
   for arg in args:
      suma +=arg
   print('La suma de la tupla',args,'es:',suma,'\n')

sumatoria(1,2,3,4,5,6,7)

def indeterminados_posicion(*args):
   print('Los datos de lo argumento y que son una tupla son:')
   for arg in args:
      print(arg)

indeterminados_posicion(5, 'hola', [1,2,3,4,5,6,7])

# ARGUMENTOS INDETERMINADOS (esto **args retorna un dicionario)
print("\nProbando el **args como argumento")
def dos_asterisco(**args):
   print(args,'ahora su clave y valor son ')
   for arg in args:
      print(arg,'=>',args[arg])

dos_asterisco(n=1,c='hola',l=['1',2,'3',4,'5'])
