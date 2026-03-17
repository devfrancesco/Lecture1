# Scrivere una classe Cliente che abbia i campi "nome", "email", "categoria" ("Gold", "Silver", "Bronze").
# vorremmo che questa classe avesse un metodo chiamato "descrizione"
# che deve restituire una stringa formattata ad esempio
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"
from dataclasses import dataclass

# Si modifichi la classe cliente in maniera tale che la proprietà categoria sia "corretta"
# e accetti solo ("Gold", "Silver", "Bronze")

categorie_valide = {"Gold", "Silver", "Bronze"}

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

@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str

    def __str__(self):
        return f"{self.name} -- {self.categoria} -- {self.email}"

def _test_modulo():
    c1 = Cliente(name="Mario Bianchi", email="mario.bianchi@polito.it", categoria="Gold")
    #c2 = Cliente(name="Carlo Masone", email="dgvasb@gmail.com", categoria="Platium")
    print(c1.descrizione())

if __name__ == "__main__":
    _test_modulo()
