### Higher Order Function ###

from functools import reduce

# Una función llama a otra función  

def sum_one(value):
  return value + 1

def sum_five(value):
  return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
  return f_sum (first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###

def sum_ten(original_value):
  def add(value):
    return value + 10 + original_value
  return add
  
add_closures = sum_ten(1)
print (add_closures(5))
print (sum_ten(5)(1))

# Built-in Higher Order Functions #


# MAP

numbers = [2, 5, 10, 21]


def multiply_two(number):
  return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# FILTER

def filter_greater_that_ten(number):
  if number > 10:
    return True
  else:
    return False

print (list(filter(filter_greater_that_ten, numbers)))
print (list(filter(lambda number: number > 10, numbers)))

# REDUCE

def sum_two_values(first_value, second_value):
  print (first_value)
  print (second_value)

  return first_value + second_value 

print (reduce(sum_two_values ,numbers))
print (reduce(lambda first_value, second_value: first_value + second_value ,numbers))