class Prodotto:
  def __init__(self, nome, prezzo, scorta):
    self.nome = nome
    self.prezzo = prezzo
    self.scorta = scorta
class GestoreMagazzino:
  def __init__(self, costo_magazzinaggio):
    self.prodotti = {}
    self.costo_magazzinaggio = costo_magazzinaggio

  def aggiungi_prodotto(self, prodotto):
    self.prodotti[prodotto.nome] = prodotto

  def rimuovi_prodotto(self, nome_prodotto):
    self.prodotti.pop(nome_prodotto)

  def calcola_costi_magazzinaggio(self):
    costi = 0
    for nome, prodotto in self.prodotti.items():
      costi += prodotto.scorta * self.costo_magazzinaggio
    return costi
p1 = Prodotto("Telefono", 500, 10)
p2 = Prodotto("Computer", 1000, 5)

gm = GestoreMagazzino(10)

gm.aggiungi_prodotto(p1)
gm.aggiungi_prodotto(p2)

print(gm.calcola_costi_magazzinaggio()) 

gm.rimuovi_prodotto("Telefono")

print(gm.calcola_costi_magazzinaggio())