#Fizzbuzz#


# Solo buzz

# def fizz():
#   for index in range(1, 101):
#     if index % 3 == 0:
#       print("fizz")
#     else:
#       print(index)

# Solo fizz

# def fizz():
#   for index in range(1, 101):
#     if index % 5 == 0:
#       print("buzz")
#     else:
#       print(index)

# Fizz, Buzz, Fizzbuzz
def fizzbuzz():
  for index in range(1, 101):
    if index % 3 == 0 and index % 5 == 0:
      print(f"fizzbuzz {index}")
    elif index % 3 == 0:
      print(f"fizz {index}")
    elif index % 5 == 0:
      print(f"buzz {index}")
    else:
      print(index)

fizzbuzz()