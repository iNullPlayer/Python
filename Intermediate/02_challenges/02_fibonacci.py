#Fibonacci#

def fibonacci():
  
  prev = 0
  next = 1
  
  for index in range(1, 51):
    # print(index)
    print(prev)

    
    fib = prev + next
    prev = next
    next = fib

fibonacci()