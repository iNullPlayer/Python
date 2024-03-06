### Variables ###

my_string_variable = ("My String variable")
print (my_string_variable)

my_int_variable = 3
print (my_int_variable)

my_bool_variable = False
print (my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print (my_int_to_str_variable)
print (type(my_int_to_str_variable))

#Concatenación de Variables en un print
print(type(print (my_string_variable, my_int_variable, my_bool_variable)))
print("Este es el valor de: ", my_bool_variable)

#Funciones del sistema
print(len(my_string_variable + my_int_to_str_variable))

#Variables de una sola linea

name, last_name, alias, age = "Sebastian", "Pacheco", "Suky", 18

print ("me llamo", name, last_name, "tambien llamado", alias, " tengo", age, "años")

print (f"Me llamo {name} {last_name} tambien llamado {alias}, tengo {age} años ")

# name = input ("Cual es tu nombre? ")
# age = input (f"Hola {name}, cual es tu edad? ")
# print (f"muy bien eres {name} con {age} años de edad")

#Cambio de tipo

name = 35
age = "Sebastian Pacheco"
print (name)
print (age)

#Forzar tipo
address: str = "Mi dirección"
address = 32
print (type(address))