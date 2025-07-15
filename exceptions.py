lista = [1,2,3,4,5,6,7,8,9,10]
search = int(input("Posizione dell'elemento che vuoi vedere nella lista?\n"))
try:
    print("elemento: ",lista[search])
except IndexError: #we can add as much as exceptions we want
    print("posizione inesistente")
else: #if we use finally instead of else, the line will be executed whether there's the exception or not
    print("elemento trovato con successo")