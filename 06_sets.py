### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Supuestamente es un diccionario

my_other_set = {"Sebastian", "Pacheco", 18, 1.73}
print (type(my_other_set))
 
print (len(my_other_set))

# print(my_other_set[0])

my_other_set.add("Suky") 

print (my_other_set) #Un set no es una estructura ordenada


my_other_set.add("Suky") #Un set no admite repetidos

print (my_other_set)

print ("Pacheco" in my_other_set)
print ("Pachecho" in my_other_set)

my_other_set.remove("Pacheco")
print (my_other_set)

my_other_set.clear() #Clear vacia todo los elementos
print (len(my_other_set))

del my_other_set #Del borra todo 

my_set = {"Sebastian", "Pacheco", 18, 1.73}

my_set = list (my_set)
print (my_set)
print (type(my_set))
 

my_set.insert(0, "Hola mundo")
print (my_set)

my_set = set(my_set)
print (type(my_set))

my_other_set = {"Golang", "Python", "JavaScript"}

my_new_set = my_set.union(my_other_set).union({"C#", "Swift"})
print (my_new_set) #Con el union se pueden agregar mas tipos

print (my_new_set.difference(my_set))