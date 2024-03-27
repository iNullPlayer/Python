### Classes ###

class MyEmptyPerson:
  pass # Pass sirve para omitir una parte de codigo

print (MyEmptyPerson)
print (MyEmptyPerson())

# Manera #1
class Person:
  def _init(self, name, last_name): # el __init_(self, <...>) es obligatorio para crear un constructor
     self.name = name
     self.last_name = last_name
  
my_person = Person("Sebastian", "Pacheco")
print(f"{my_person.name} {my_person.last_name}")

# Manera #2
class Person:
  def _init(self, name, last_name, alias = "Sin alias"): # el __init_(self, <...>) es obligatorio para crear un constructor
     self.full_name = f"{name} {last_name}, {alias}" # Propiedad Publica
     self.__name = name # Propiedad Privada
     self.__last_name = last_name
  
  def walk(self): # Self es obligatorio
     print(f"{self.full_name} esta caminando")
  
  def get_name(self):
     return self.__name


my_person = Person("Sebastian", "Pacheco", "Suky")
print(my_person.full_name)
print(my_person.get_name)


my_person.walk()

my_other_person = Person("Jilver", "Pacheco", "Razziel")
print(my_other_person.full_name)
print(my_other_person.get_name())



# my_other_person.walk()

# my_other_person.full_name = ("Jilver Pacheco, No-Name") # Las clases se pueden modificar desde fuera de ellas
# print(my_other_person.full_name)