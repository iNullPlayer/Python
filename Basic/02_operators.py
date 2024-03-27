### Operadores Aritméticos ###

#Operadores básicos
#Suma
print (2 + 2) 
#Resta
print (2 - 2)
#Multiplicación
print (2 * 2)
#División
print (2 / 2)
#Residuo de la división
print (10 % 3)
#División entera
print (10 // 3)
#Potenciación
print (2 ** 3)

print ("")

#Operadores Aritméticos con Cadenas de texto
print ("Hola " + "Mundo") 
print ("Hola " + str(5)) 
print ("Hola " * 5)
print ("Hola " * (3 ** 2))
my_float = 2.5 * 2
print ("Hola " * int(my_float))

print ("")

###Operadores Comparativos###
#Mayor
print (3 > 4)
#Menor
print (3 < 4)
#Mayor o igual
print (3 >= 4)
#Menor o igual
print (3 <= 4)
#Igual
print (3 == 4)
#Diferente
print (3 != 4)

print ("")

#Operadores Comparativos (Inverso)
#Mayor
print (not(3 > 4))
#Menor
print (not(3 < 4))
#Mayor o igual
print (not(3 >= 4))
#Menor o igual
print (not(3 <= 4))
#Igual
print (not(3 == 4))
#Diferente
print (not(3 != 4))

print ("")

#Operadores Comparativos con cadenas de texto
#Cuentan la cantidad de caracteres que se esta usando, por la ordenación alfabética y también por las mayúsculas. Es diferente de "len"
print ("Hola" > "Mundo")
#Menor
print ("Hola" < "Mundo")
#Mayor o igual
print ("Hola" >= "Mundo")
#Menor o igual
print ("Hola" <= "Mundo")
#Igual
print ("Hola" == "Mundo")
#Diferente
print ("Hola" != "Mundo")
#Ejemplos de la ordenación alfabética
print ("aaaa" >= "aaba")
print ("aaaa" >= "aaaa")
#Ejemplo de mayúsculas
print ("AAAA" >= "aaaa")
print ("aaaa" >= "AAAA")

print ("")

###Operadores Lógicos###
print (3 > 4 and "Hola" > "Mundo")
print (3 > 4 or "Hola" > "Mundo")
print (3 < 4 and "Hola" < "Mundo")
print (3 < 4 or "Hola" < "Mundo")
print (not(3 > 4, "Hola" > "Mundo")) #Inverso