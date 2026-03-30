from dataclasses import dataclass


@dataclass
class ClienteRecord:
    name: str
    mail: str
    categoria: str

    def __hash__(self): #se due clienti hano stessa mail, allora hanno stesso hash
        return hash(self.mail) #chiave primaria

    def __eq__(self, other):
        self.mail == other.mail

    def __str__(self):
        return f"{self.name} -- {self.categoria} -- {self.mail}"