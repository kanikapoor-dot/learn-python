# if condition
price = float(input("Amount : "))

if price >= 1.00:
    print('Tax + price ${}'.format(price+(price * 0.007)))
else:
    print(f'Price ${price}')

# Note: careful of string comparision (its case sensitive)

# Nested if else
#-----------------

# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

#Complex condition
#-------------------

# if condition and condtion :
#     statement 
# else:
#     statement