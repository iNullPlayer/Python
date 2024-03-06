### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_other_tuple = (18, 30, 60)
my_tuple = (18, 1.73, "Sebastian", "Pacheco", "Pacheco")
print(my_tuple)
print(type(my_tuple))

print (my_tuple[0])
print (my_tuple[-1])

print (my_tuple.count("Pacheco"))
print(my_tuple.index("Pacheco"))

#las tuples son inmutables
# my_tuple[1] = 1.80
# print (my_tuple)

#Nueva Tuple
my_sum_tuple = my_tuple + my_other_tuple
print (my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Hola mundo"
my_tuple.insert(1, "Red")
my_tuple = tuple(my_tuple)
print (type(my_tuple))
print (my_tuple)

del my_tuple