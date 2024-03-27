# hacer un "¿Es un numero primo?" #

def is_prime():
  
  for number in range (1, 101):
  
    if number >= 2:
      is_divisible = False
  
      for index in range (2, number):
        if number % index == 0:
          is_divisible = True

      if not is_divisible:
        print(number)

is_prime()