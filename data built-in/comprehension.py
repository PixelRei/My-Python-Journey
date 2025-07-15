import math
#comprehension is a way to create a set, dict or a list in a more specific way
#for lists
lista = [x**2 for x in range(11)]
print(lista)

#for set
s = {int(math.sqrt(x)) for x in lista}
print(s)

#and for dict
dict = {c: c.upper() for c in 'abcd'}
print(dict)

#we can also combine with other ifs or for 