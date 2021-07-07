first = 'kani'
last = 'kapoor'
print(first + ' ' + last)  

sentences = "hello i'm do learning for passion do el savodora" 
print(sentences.upper())
print(sentences.lower())
print(sentences.capitalize())
print(sentences.count('el'))

# python string format

output = ('Hello {1} {0}').format(last,first)
output = f'Hola {first} {last} {15}'
print(output)