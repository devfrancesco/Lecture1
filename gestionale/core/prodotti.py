from dataclasses import dataclass


class Prodotto:
    aliquota_iva = 0.22 #variabile di classe -- ovvero è la stessa per tutte le istanze che verrano create.

    def __init__(self, name: str, price: float, quantity: int, supplier = None):
        self.name = name
        self._price = None
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self._price * self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto * (1 + self.aliquota_iva)
        return lordo

    @classmethod #costruisce un nuovo costruttore
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str):
        return cls(name, price, 1, supplier)

    @staticmethod #non sono associati a nessuna istanza
    def applica_sconto(prezzo, percentuale):
        return prezzo * (1-percentuale)

    @property
    def price(self): #equivalente a getter
        return self._price

    @price.setter
    def price(self, valore): #setter
        if valore < 0:
            raise ValueError("Attenzione il prezzo non può essere negativo.")
        self._price = valore

    def __str__(self):
        return f"{self.name} - disponibili {self.quantity} pezzi a {self.price}$"

    def __repr__(self):
        return f"Prodotto(name={self.name}, price= {self.price}, quantity={self.quantity}, supplier={self.supplier})"

    def __eq__(self, other: object):

        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    def __lt__(self, other:"Prodotto") -> bool :
        return self.price < other.price

    def prezzo_finale(self) -> float:
        return self.price * (1+self.aliquota_iva)

class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price: float, quantity: int, supplier: str, sconto_percento: float):
        #Prodotto.__init__()
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self) -> float:
        return self.valore_lordo() * (1-self.sconto_percento/100)

class Servizio(Prodotto):
    def __init__(self,name: str, tariffa_oraria: float, ore: int):
        super().__init__(name=name, price= tariffa_oraria, quantity=1, supplier=None)
        self.ore=ore

    def prezzo_finale(self) -> float:
        return self.price * self.ore

class Abbonamento:
    def __init__(self, nome:str, prezzo_mensile: float, mesi:int):
        self.name = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return self.prezzo_mensile * self.mesi

@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

    def __hash__(self):
        return hash((self.name, self.prezzo_unitario))

    def __str__(self):
        return (f"{self.name} -- {self.prezzo_unitario}")

MAX_QUANTITA = 1000

def crea_prodotto_standard(nome:str, prezzo: float):
    return Prodotto(nome,prezzo, 1, None)

def _test_modulo():
    print("Sto testando il modulo prodotti.py")
    myproduct1 = Prodotto(name="Laptop", price=1200.0, quantity=12, supplier ="ABC")

    print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

    print (f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}") #uso un metodo di istanza
    p3 = Prodotto.costruttore_con_quantità_uno("Auricolari", 200.0, "ABC" ) #modo per chiamare un metodo di classe

    print(f"Prezzo scontato di myprocuct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}") # modo per chiamare un metodo statico
    myproduct2 = Prodotto(name="Mouse", price=10, quantity=25, supplier="CDE")
    print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")
    Prodotto.aliquota_iva = 0.24
    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")

    print(myproduct1)

    p_a = Prodotto(name="Laptop", price=1200.0, quantity=12, supplier ="ABC")
    p_b = Prodotto("Mouse", 10, 14, "CDE")

    print("myproduct1 == p_a?", myproduct1 == p_a) #va a chiamare il metodo __eq__ appena implementato. Mi aspetto TRUe
    print("p_a == p_b?", p_a == p_b) #Mi aspetto FALSE

    mylist = [p_a, p_b, myproduct1]
    mylist.sort(reverse=True)

    print("lista di prodotti ordinata")
    for i in mylist:
        print(f"- {i}")

if __name__ == "__main__":
    _test_modulo()