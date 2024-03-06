### List ###

my_list = list ()
my_other_list = []

print (len(my_list))

my_list = [18, 24, 62, 52, 30, 30, 17]

print (my_list)
print (len(my_list))

my_other_list = [35, 1.73, "Sebastian", "Pacheco"]
print (my_other_list)
print(type(my_other_list))
print(type(my_list))

#las listas inician desde 0
print (my_other_list[0])
print (my_other_list[1])
print (my_other_list[-1])
print (my_other_list[-3])
print (my_other_list.count("Pacheco"))
print (my_list.count(30))

age, height, name, last_name = my_other_list

print(name)

name, height, age, last_name = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3],

print(name)

print  (len(my_list + my_other_list))
print (my_list + my_other_list)

# my_list = "Hola mundo"
print (my_list)
print (type(my_list))

my_other_list.append("MoureDev")
print (my_other_list)

my_other_list.insert(1, "Blue")
print (my_other_list)

my_other_list[1] = "Red"
print (my_other_list)

my_other_list.remove("Red")
print (my_other_list)

my_list.remove(30)
print(my_list)

#Con pop ( ) se elimina un elemento en una posición determinada (ver arriba). remove ( ) elimina el primer elemento con un valor determinado.
print(my_list.pop())
print(my_list)
print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print (my_pop_element)
print (my_list)

del my_list[2]
print (my_list)

my_new_list = my_list.copy()
print (my_new_list)
print (my_list)


my_list.clear()
print (my_list)
print (my_new_list)

my_new_list.reverse()
print (my_new_list)

my_new_list.sort()
print (my_new_list)

print (my_new_list[0:2])