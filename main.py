# Scriviamo un codice python che modelli un semplice
# gestionale aziendale. Dovremmo provvedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente
# scontati, ...


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
        cls(name, price, 1, supplier)

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

# Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
# vorremmo che questa classe avesse un metodo chiamato "descrizione"
# che deve restituire una stringa formattata ad esempio
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"

# Si modifichi la classe cliente in maniera tale che la proprietà categoria sia "corretta"
# e accetti solo ("Gold", "Silver", "Bronze")

class Cliente:
    def __init__(self, name, email, categoria):
        self.name = name
        self.email = email
        self._categoria = None
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        categorie_valide = {"Gold", "Silver", "Bronze"}
        if categoria not in categorie_valide:
            raise ValueError("Categoria non valida. Scegliere tra Gold,Silver,Bronze")
        self._categoria = categoria

    def descrizione(self): #toPrint di java
        return f"Cliente {self.name} ({self.categoria}) - {self.email}"

c1 = Cliente(name="Mario Bianchi", email="mario.bianchi@polito.it", categoria="Gold")
c2 = Cliente(name="Carlo Masone", email="dgvasb@gmail.com", categoria="Platium")
print(c1.descrizione())

