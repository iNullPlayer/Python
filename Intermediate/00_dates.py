### Dates ###

import datetime

from datetime import datetime

def print_date(date):
  print (date.year)
  print (date.second)
  print (date.minute)
  print (date.hour)
  print (date.day)
  print (date.month)
  print (date.timestamp())

Now = datetime.now()
print (Now.second, Now.minute, Now.hour, Now.day, Now.month)

timestamp = Now.timestamp(  )
print (timestamp)

year_2025 = datetime(2025, 1, 1, 0, 0, 0)

print_date(year_2025)

print_date(Now)

from datetime import time

current_time = time(2, 17, 40)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date

# Coloca el dia de hoy
current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Coloca el dia dado

current_date = date(2024, 3, 14)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 1, current_date.month + 1, current_date.day + 1)

print(current_date.year)
print(current_date.month)
print(current_date.day)

driff = year_2025 - Now
print(driff)

# Time delta sirve mas para servicios de suscripción
from datetime import  timedelta

start_time_delta = timedelta(200, 100, 100, weeks = 10)
end_time_delta = timedelta(300, 100, 100, weeks = 13)

print (end_time_delta - start_time_delta)
