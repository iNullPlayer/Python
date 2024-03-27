### Functions ###

def my_function (): 
  print ("Hola mundo")
  
my_function()

def sum (a, b): # Establecer un tipado no sirve de nada, pero por buena practica deberías ponerlo. Ayuda a tus compañeros de trabajos a saber tipo usas
  print (a + b)  
  
sum(1.5, 1.7) 

def sum_with_return (a, b): # Esto es igual a esto ↓
  return (a + b) 

def sum_with_return (a, b): # Esto es igual a esto ↑
  my_sum = a + b
  return my_sum

my_result = sum_with_return(2, 1)
print(my_result)

def print_name (name, last_name):
  print(f"Hola mi nombre es {name} y mi apellido es {last_name}")

print_name("Sebastian", "Pacheco")

def print_name_with_default (name, last_name, alias = "No-name"):
  print(f"Hola mi nombre es {name} y mi apellido es {last_name}, alias: {alias}")

print_name_with_default("Sebastian", "Pacheco")
print_name_with_default("Sebastian", "Pacheco", "Suky")

def print_text(*text):
  for text in text:
    print (text)
  
print_text("Hola", "Mundo")

def print_upper_texts(*texts):
  for text in texts:
    print (text.upper())
  
print_upper_texts("Hola", "Mundo")