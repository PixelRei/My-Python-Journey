#reversing a list
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista.reverse()) #!!! it doesn't return the list, it just reverses it
print(lista)

#ordinates a list from the lower to the highest value
lista.sort()
print(lista)

#getting a copy of a list
copy_list = lista.copy()

#and finally removing all the items of the list
lista.clear()
print(lista)