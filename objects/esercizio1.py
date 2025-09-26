#Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso. 
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona, ad esempio
#  “Ciao, mi chiamo Marco e ho 32 anni”.
class Persona:
    def __init__(self, nome, età, sesso):
        self.nome = nome
        self.età = età
        self.sesso = sesso
    def presentati(self):
        print("Ciao, mi chiamo ", self.nome, " e ho ", self.età, " anni" )

persona = Persona("Marco", 32, "M")
persona.presentati()