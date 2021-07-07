# working with datetime library to use datetime function
from datetime import datetime

current_day = datetime.now()
print(f'Today : {current_day}' )

#timedelta function had used for go back through

from datetime import timedelta

one_day = timedelta(days=1)
yesterday = current_day - one_day
print(f'Yesterday : {yesterday}')

#last week this day 
# #possible arguments 
# timedelta(days: float, seconds: float, \
#     microseconds: float, milliseconds: float, \
#     minutes: float, hours: float, weeks: float)
week_day = timedelta(weeks=1)
print(f'Last week : {current_day-week_day}')

# Now datetime specfic values
print('Day : '  + str(current_day.day))
print('Month : '+ str(current_day.month))

# Here complexity goes converting str into datetime format 
u_bday = input('When is your birthday (dd/mm/yyyy)')

birthday = datetime.strptime(u_bday,'%d/%m/%Y')

#Age calculator
print(f'Age : {current_day.year-birthday.year}') 
