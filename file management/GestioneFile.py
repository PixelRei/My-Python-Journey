numeri = open("file.txt")
lista = []
lista.extend(numeri)
n1 = int(lista[0])
n2 = int(lista[1])
risultato = open("risultato.txt", "w")
risultato.write(str(n1+n2))