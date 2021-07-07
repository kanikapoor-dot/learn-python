x = 0
y = 2
# print(y/x) # throws zerodivison error


#creating age calc birthday format error and resolve it 
from datetime import datetime

today = datetime.now()

birthday = input('When your birthday ?? (dd/mm/yyyy)')

try:
   global bday
   bday = datetime.strptime(birthday,'%d/%m/%Y')
   print(f'Your Age : {today.year-bday.year}')
except ValueError as e:
    print(e)
finally:
    print('It happens')
  