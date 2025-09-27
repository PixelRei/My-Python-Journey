import re

def WordCounter(frase):
    parole2 = {}
    parole1 = re.split(r"[!?.,\s]+", frase.lower().strip())
    for parola in parole1:
        if parola  not in parole2:
            parole2[parola] = 1
        else:
            parole2[parola] += 1
    return parole2


frase = input("Digita una frase: \n")
print(WordCounter(frase))