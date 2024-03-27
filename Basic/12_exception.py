### Exceptions Handling ###

# Try y Except son obligatorios
# Else es opcional o dependiendo de la accion
# Finally opcional y se ejecuta siempre

number1, number2 = 5, 1

number2 = "2"

#Try - Except

try:
  print (number1 + number2)
  print ("No se a producido un error")
except:
  print ("Se a producido un error")

#Try - Except - Else
  
try:
  print (number1 + number2)
  print ("No se a producido un error")
except:
  print ("Se a producido un error")
else:
  print("La ejecucion continua correctamente")

#Try - Except - Else - Finally

try:
  print (number1 + number2)
  print ("No se a producido un error")
except:
  print ("Se a producido un error")
else:
  print ("La ejecucion continua correctamente")
finally:
  print ("La ejecucion termina")

# Excepciones por tipo

try:
  print (number1 + number2)
  print ("No se a producido un error")
except ValueError:
  print ("Se a producido un ValueError")
except TypeError:
  print ("Se a producido un TypeError")

# Captura de la informacion de la excepcion

try:
  print (number1 + number2)
  print ("No se a producido un error")
except ValueError as error:
  print ("Se a producido un ValueError")
  print (error)
except TypeError as error:
  print ("Se a producido un TypeError")
  print (error)
except Exception as exception:
  print ("Se a producido un Exception")
  print (exception)