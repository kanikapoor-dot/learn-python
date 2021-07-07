#collection
#-------------

# List - [] which stores any DATATYPE 

ini = ['a','b'] #initiated list
scores = [] #Empty list
scores.append(5)
scores.append('a')
print(ini)
print(scores)

# ['a', 'b']
# [5, 'a']

print()
print()

#  Array - which stores only defined DATATYPE

from array import array

sc = array('d') 
# array('d') means array the function 
# 'd' - double, datatype which only allowed to store in this array 
# we can use 'i', for integer and refer for more datatypes
sc.append(31)
sc.append(32)

# sc.append('a')    
#error 👆

# Traceback (most recent call last):
#     sc.append('a')
# TypeError: must be real number, not str

print(sc[0])

print()
print()

# List fuctionality
names = ['kni','sa','ch','bs']
names.insert(1,'vi')
print(names)
names.sort()
print(names)
print(names[-3:])

print()
print()

#dictionary - {} key,value pairs 
# differents between dict and list is dict
#  not garanteed order storage but list does


hel = {'first':'kani'}
hel['last'] = "kapoor"
hel[3] = 'hi'
hel['ho'] = 2
hel[2] = 4
print(hel)