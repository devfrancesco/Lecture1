from dataclasses import dataclass

from gestionale.core.clienti import Cliente
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine
from datetime import date



@dataclass
class Fattura:
    ordine: "Ordine"
    numero_fattura: str
    data: date

    def genera_fattura(self) -> str:
        """Genera il testo della fattura."""
        linee = [
            "="*60,
            #intestazione della fattura, ovvero data e num fattura
            f"FATTURA N. {self.numero_fattura}".center(60),
            f"Data: {self.data.strftime('%d/%m/%Y')}".center(60),
            f"=" * 60,
            "",
            #dettagli del cliente
            f"Cliente: {self.ordine.cliente.name}",
            f"Categoria: {self.ordine.cliente.categoria}",
            f"Mail: {self.ordine.cliente.email}",
            "",
            "-"*60,
            f"DETTAGLIO PRODOTTI",
            "-"*60
        ]
        for i, riga in enumerate(self.ordine.righe,1): #Inizia da 1 la numerazione
            linee.append(
                f"{i}. {riga.prodotto.name:<22}"
                f"Q.tà {riga.quantita:>3} x {riga.prodotto.prezzo_unitario:>8.2f} = "
                f"Tot. {riga.totale_riga():>10.2f}$"
            )

        linee.extend([
            "-"*60,
            "",
            f"Totale netto: {self.ordine.totale_netto()}",
            f"IVA (22%): {self.ordine.totale_netto()*0.22}",
            f"Totale lordo: {self.ordine.totale_lordo(0.22)}",
            "",
            "=" * 60]
        )
        return "\n".join(linee)

def _test_modulo():
    p1 = ProdottoRecord("Laptop", 1200.0)
    p2 = ProdottoRecord("Mouse", 20.0)
    p3 = ProdottoRecord("Tablet", 600.0)
    cliente = Cliente("Mario Bianchi", "mario.bianchi@polito.it", "Gold")
    ordine = Ordine(righe =[
        RigaOrdine(p1, 1),
        RigaOrdine(p2, 5),
        RigaOrdine(p3, 2)
    ], cliente=cliente)
    fattura = Fattura(ordine,"2026/01", date.today())

    print(fattura.genera_fattura())

if __name__ == "__main__":
    _test_modulo()