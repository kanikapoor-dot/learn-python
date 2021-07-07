# cant concatenate numbers with strings while print statement

print(str(0) + ' zero')

#getting input from and convert that into number datatypes

first_number = input('First Number : ')
second_number = input('Second Number : ')
 
#this returns every user inputted value has 
#first become string we have to convert it
print(type(first_number))
print(type(int(second_number)))

print(first_number + second_number)
print(int(first_number)+int(second_number))