### Strings ###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print (len(my_string))
print (len(my_other_string))

print (my_string + " " + my_other_string)

my_new_line_string = "Este es un string \ncon salto de linea"
print (my_new_line_string)

my_tap_string = "\tEste es un string con tabulación"
print (my_tap_string)

my_scape_string = "\\tEste es un string escapado \\n escapado"
print (my_scape_string)

#Formateo

name, last_name, age = "Sebastian", "Pacheco", 18

print ("Mi nombre es {} {} con {} años de edad".format(name, last_name, age))
print ("Mi nombre es %s %s con %d años de edad"%(name, last_name, age)) #Esta forma es mejor y mas segura cuando se usan strings y números 
print (f"Mi nombre es {name} {last_name} con {age} años de edad") #Manera rápida
print ("Mi nombre es " + name + " " + last_name + " " + "con " + str(age) + " años de edad") #Ni loco hagas esta

#Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f  = language
print (a)
print (b)
print (a, b, c, d, e, f)

#División 
language_slice = language[1:3]
print (language_slice)
language_slice = language[1:]
print (language_slice)
language_slice = language[-3]
print (language_slice)
language_slice = language[1:2:4]
print (language_slice)

#Reverse
reversed_language = language[::-1]
print (reversed_language)

#Métodos/Funciones

print (language.capitalize()) #Primera letra en mayúsculas
print (language.upper()) 
print (language.lower()) 
print (language.count("t")) 
print (language.isnumeric()) 
print ("1".isnumeric()) 
print (language.upper().isupper()) 
print (language.lower().isupper()) 
print (language.startswith("Py")) 



