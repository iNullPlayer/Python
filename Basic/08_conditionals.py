### Conditionals ###

my_condition = True

if my_condition: # es igual a "if <...> == True:"
  print ("Se ejecuto la condición del if")
else:
  print ("No se ejecuto")

print ("")

my_condition = 5 * 2 

if my_condition == 10:
  print ("Si es 10")
else:
  print ("No es 10")
  
print ("")

if my_condition >= 10:
  print ("Si es mayor o igual a 10")
else:
  print ("No es mayor o igual a 10")
  
print ("")

my_condition = 15

if my_condition > 10 and my_condition < 20: # If para inicializar una condición de ejecución (Inicializador)
  print ("Esta entre 10 y 20")
elif my_condition == 1: # elif para ejecutar una condición verdadera en especifico (Reserva del if)
  print ("Es igual a 1")
else: # else para ejecutar una condición final (Si el if o el elif no funcionan)
  print ("No esta entre 10 y 20 o distinto de 1")
  
print ("")

my_string = "" # Un string vacío es igual a False

if my_string:
  print("Mi cadena de texto es Tiene algo")
else:
  print("Mi cadena de texto es vacía")   

print ("")

my_string = "Hola mundo"

if my_string == "Hola mundo":
  print("Hola mundo")
else:
  print("Adios mundo")
  
print ("")

my_string = "Hola mundo"

if not my_string == "Hola mundo":
  print("Hola mundo")
else:
  print("Adios mundo")
  
# my_condition = 10

# if my_condition == 10 or my_condition in range(100, 201):
#     print("Es igual a 10 o está entre 100 y 200")
# else:
#     print("No es igual a 10 o no está entre 100 y 200")
