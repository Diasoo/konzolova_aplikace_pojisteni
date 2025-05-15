# evidence.py
from pojistenec import Pojistenec

class Evidence:
    """
    Spravuje seznam pojištěnců a umožňuje s nimi provádět operace.
    """
    def __init__(self):
        """
        Inicializuje instanci třídy Evidence prázdným seznamem pojištěnců.
        """
        self.seznam_pojistenych = []

    def __str__(self):
        """
        Vrací řetězcovou reprezentaci seznamu pojištěnců pro výpis.
        """
        return "\n".join(str(pojistenec) for pojistenec in self.seznam_pojistenych)

    def vytvor_pojistence(self, jmeno, prijmeni, vek, telefon):
        """
        Vytvoří nového pojištěnce a přidá ho do seznamu pojištěnců.

        Args:
            jmeno (str): Křestní jméno pojištěnce.
            prijmeni (str): Příjmení pojištěnce.
            vek (int): Věk pojištěnce.
            telefon (str): Telefonní číslo pojištěnce.
        """
        self.seznam_pojistenych.append(Pojistenec(jmeno, prijmeni, vek, telefon))

    def vypis_pojistence(self):
        """
        Vrátí seznam všech pojištěnců.

        Returns:
            list: Seznam objektů třídy Pojistenec.
        """
        return self.seznam_pojistenych

    def najdi_pojistence(self, jmeno, prijmeni):
        """
        Vyhledá pojištěnce v seznamu podle jména a příjmení (case-insensitive).

        Args:
            jmeno (str): Křestní jméno hledaného pojištěnce.
            prijmeni (str): Příjmení hledaného pojištěnce.

        Returns:
            list: Seznam nalezených pojištěnců, kteří odpovídají zadanému jménu a příjmení.
                  Pokud žádný pojištěnec nebyl nalezen, vrací prázdný seznam.
        """
        jmeno = jmeno.lower().strip()
        prijmeni = prijmeni.lower().strip()
        return [osoba for osoba in self.seznam_pojistenych if
                osoba.jmeno.lower() == jmeno and osoba.prijmeni.lower() == prijmeni]

    def vymaz_pojistence(self, jmeno, prijmeni):
        """
        Odstraní pojištěnce ze seznamu podle jména a příjmení.

        Args:
            jmeno (str): Křestní jméno pojištěnce k odstranění.
            prijmeni (str): Příjmení pojištěnce k odstranění.

        Returns:
            bool: True, pokud byl pojištěnec odstraněn, False jinak.
        """
        jmeno = jmeno.lower().strip()
        prijmeni = prijmeni.lower().strip()
        delka_seznamu = len(self.seznam_pojistenych)
        self.seznam_pojistenych = [osoba for osoba in self.seznam_pojistenych if
                                    osoba.jmeno.lower() != jmeno or
                                    osoba.prijmeni.lower() != prijmeni]
        if len(self.seznam_pojistenych) == delka_seznamu:
            return False
        return True