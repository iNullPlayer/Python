### Loops ###

# While: puede llegar a ser una iteración infinita si no se rompe el ciclo

# my_condition = 0  

# while my_condition < 10:
#   print(my_condition) 
#   my_condition += 1 # += <numero> sirve para sumar el numero anterior por el mismo numero de siempre. Ej: 0 + 1 = 1 + 1 = 2 + 1...  
# else: # Funciona solo el else. El if y el elif no. Aparte es opcional
#   print ("Condición igual 10")
  
# print("")

# while my_condition <= 19:
#   my_condition += 1
#   if my_condition == 15:
#     print ("Se detiene")
#     break
#   print(my_condition)
  
# For: es una iteración finita que solo lee los datos dados

my_list = [18, 24, 62, 52, 30, 30, 17]
my_tuple = (18, 1.73, "Sebastian", "Pacheco", "Pacheco")
my_set = {"Sebastian", "Pacheco", 18, 1.73}
my_dict = {
  "Nombre": "Sebastian", 
  "Apellido": "Pacheco", 
  "Edad": 35, 
  "Lenguajes": {"Python","Swift", "JavaScript"},
  1: 1.73
  }

for item in my_list:
  print (item)

print("")

for item in my_tuple:
  print (item)
  
print("")
  
for item in my_set:
  print(item)
  
print("")

for item in (my_dict):
  print(item)
  if item == "Edad":
    print("Se ejecuto la edad")
    break # EVITAR EL CONTINUE, es una mala practica
  elif item == 1:
    print("Item vale 1")
else:
  print ("Bucle terminado")
  
print("")

