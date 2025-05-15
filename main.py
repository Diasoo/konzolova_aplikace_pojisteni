from evidence import Evidence
from ui import zobraz_menu, zobraz_pojistence
from validatory import zadej_vek, zadej_beznou_hodnotu, zadej_telefon


evidence = Evidence()

HLAVICKA = f"{'Jméno':<15}\t {'Příjmení':<15}\t {'Věk':<5}\t {'Telefon':<15}\t"
NENALEZEN = "Žádný pojištěnec nebyl nalezen."
DEKORATOR = "-" * len(HLAVICKA)

def main():
    """
    Hlavní funkce programu pro evidenci pojištěnců.
    Zobrazuje menu a umožňuje uživateli provádět akce jako přidávání,
    vypisování a vyhledávání pojištěnců.
    """
    print("Vítejte v programu pro evidenci pojištěnců.")
    akce = ""
    while akce != "5":
        zobraz_menu()
        akce = input("Zadejte číslo akce, kterou chcete provést: ").strip()

        match akce:
            case "1":
                jmeno = ziskej_a_validuj_udaje("jmeno")
                prijmeni = ziskej_a_validuj_udaje("prijmeni")
                vek = ziskej_a_validuj_udaje("vek")
                telefon = ziskej_a_validuj_udaje("telefon")
                evidence.vytvor_pojistence(jmeno, prijmeni, vek, telefon)
                print("Pojištěnec byl úspěšně přidán.")
            case "2":
                pojistenci = evidence.vypis_pojistence()
                zobraz_pojistence(pojistenci, HLAVICKA, DEKORATOR)
            case "3":
                jmeno = ziskej_a_validuj_udaje("jmeno")
                prijmeni = ziskej_a_validuj_udaje("prijmeni")
                pojistenci = evidence.najdi_pojistence(jmeno, prijmeni)
                zobraz_pojistence(pojistenci, HLAVICKA, DEKORATOR)
            case "4":
                jmeno = ziskej_a_validuj_udaje("jmeno")
                prijmeni = ziskej_a_validuj_udaje("prijmeni")
                if not evidence.najdi_pojistence(jmeno, prijmeni):
                    print("Pojištěnec nebyl nalezen.")
                    continue
                if evidence.vymaz_pojistence(jmeno, prijmeni):
                    print("Pojištěnec byl úspěšně odstraněn.")
                else:
                    print("Pojištěnce se nepodařilo odstranit.")
            case "5":
                print("Děkuji za použití programu.")
                break
            case _:
                print("Musíte zadat číslo od 1 do 5")


def ziskej_a_validuj_udaje(typ_udaje):
    """
    Získá a validuje uživatelský vstup pro zadaný typ údaje.
    """
    validovano = False
    vstup = None
    while not validovano:
        match typ_udaje:
            case "jmeno":
                vstup = input("Zadejte jméno: ")
                validovano = zadej_beznou_hodnotu(vstup, "křestní jméno")
            case "prijmeni":
                vstup = input("Zadejte příjmení: ")
                validovano = zadej_beznou_hodnotu(vstup, "příjmení")
            case "vek":
                vstup = input("Zadejte věk: ")
                try:
                    vstup = int(vstup)
                except ValueError:
                    print("Věk musí být celé číslo mezi 1 a 120.")
                    continue
                validovano = zadej_vek(vstup)
            case "telefon":
                vstup = input("Zadejte telefonní číslo: ")
                validovano = zadej_telefon(vstup)
            case _:
                raise ValueError("Neznámý typ údaje")
    return vstup

if __name__ == "__main__":
    main()