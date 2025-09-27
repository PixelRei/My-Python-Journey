#Creare una classe Animale che abbia gli attributi “nome” e “specie”. 
# Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie. 
# Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.
class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
    def emetti_suono(self):
        if self.specie.lower() == "gatto":
            print("Miao!")
        elif self.specie.lower() == "cane":
            print("Bau!")

dog = Animale("Pluto", "cane")
cat = Animale("Gato Panzone", "gatto")

dog.emetti_suono()
cat.emetti_suono()