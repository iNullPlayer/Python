### Error Types ###

# SyntaxError #
# print "Hola mundo" # ERROR
print("Hola mundo")

# NameError #
language = "Spanish" # Comentar para error
print(language)

# IndexError #
my_list = ["Python", "Swift", "JavaScript"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[3]) # ERROR
print(my_list[-1])

# ModuleNotFoundError #
# import maths # ERROR
import math

# AttributeError #
# print (math.PI) # ERROR
print (math.pi) 

# KeyError #
my_dict = {
  "Nombre":"Sebastian",
  "Apellido":"Pacheco", 
  "Edad":18, 
  1:"Python"
 }
# print(my_dict["Apelido"]) # ERROR
print(my_dict["Apellido"])

# TypeError #
# print(my_list["Nombre"]) # ERROR
print(my_list[1]) 

# ImportError #
# from math import PI # ERROR
from math import pi

# ValueError #
# my_int = int("Hola mundo") #ERROR
# print(type(my_int))

my_int = int("10")
print(type(my_int))

# ZeroDivisionError #
print(4/2)
print(4/0) # ERROR