import random

def ControllaNumero(user, n):
    cows, bulls = 0, 0
    for x in range(len(user)):
        if user[x] == n[x]:
            cows += 1
        elif user[x] in n:
            bulls += 1
    print("Cows: ", cows, " Bulls: ", bulls)
    if cows == 4:
        return True
    else: 
        return False
    
    # return True if cow == 4 else False

numeri = "1234567890"
print("Benvenuto in Cows and Bulls, prova a indovinare il numero di 4 cifre che sto pensando")
n = 0
n = [random.choice(numeri) for x in range(4)]
user = input("Inserisci un numero: ")
while not ControllaNumero(user, n):
    user = input("Inserisci un numero: ")
if ControllaNumero():
    print("Grande! Hai indovinato il numero")