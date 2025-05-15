class Pojistenec:
    """
    Reprezentuje pojištěnce s jeho osobními údaji.
    """
    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Konstruktor pro vytvoření instance pojištěnce.

        Args:
            jmeno (str): Křestní jméno pojištěnce.
            prijmeni (str): Příjmení pojištěnce.
            vek (int): Věk pojištěnce.
            telefon (str): Telefonní číslo pojištěnce.
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """
        Vrací řetězcovou reprezentaci pojištěnce pro výpis.
        """
        return f"{self.jmeno:<15}\t {self.prijmeni:<15}\t {self.vek:<5}\t {self.telefon:<15}\t"