class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

class Studente(Persona):
    def __init__(self, nome, cognome, matricola):
        super().__init__(nome, cognome)
        self.matricola = matricola

# saranno ereditati in questo modo tutti gli attributi e metodi della classe Persona
studente1 = Studente("Mario", "Rossi", "12345")
print(studente1.nome)      # Output: Mario
print(studente1.cognome)   # Output: Rossi
print(studente1.matricola)  # Output: 12345
