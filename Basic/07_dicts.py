### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print (type(my_dict))
print (type(my_other_dict))

my_other_dict = {
  "Nombre":"Sebastian",
  "Apellido":"Pacheco", 
  "Edad":35, 
  1:"Python"
 }

my_dict = {
  "Nombre": "Sebastian", 
  "Apellido": "Pacheco", 
  "Edad": 35, 
  "Lenguajes": {"Python","Swift", "JavaScript"},
  1: 1.73
  }

print (my_dict)
print (my_other_dict)

print (len(my_other_dict))
print (len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle 9"
print(my_dict)

my_dict.pop(1)
print(my_dict)

print ("Nombre" in my_dict)
print ("Pachecho" in my_dict)

print (my_dict["Apellido"])

print (my_dict.items())
print (my_dict.keys())
print (my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print (my_new_dict)

my_new_dict = dict.fromkeys((("Nombre", 1, "Piso")))
print (my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print (my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Pacheco", "Sebastian"))
print (my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ["Pacheco", "Sebastian"])
print (my_new_dict)

my_values = my_new_dict.values()
print (type(my_values))


print (my_new_dict.values())
print ("")
print (tuple(my_new_dict))
print ("")
print (set(my_new_dict))
print ("")
print (list(my_new_dict.fromkeys(list(my_new_dict.keys()))))
#no entendí el Fromkeys, Debo investigar mas