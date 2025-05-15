# ui.py
def zobraz_menu():
    """
    Zobrazuje uživateli menu s možnostmi programu.
    """
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného podle jména")
    print("4 - Odstranit pojištěného")
    print("5 - Ukončit program")

def zobraz_pojistence(pojistenci, hlavicka, dekorator):
    """
    Zobrazuje seznam pojištěnců.

    Args:
        pojistenci (list): Seznam objektů pojištěnců k zobrazení.
        hlavicka (str): Řetězec s hlavičkou tabulky pro výpis pojištěnců.
        dekorator (str): Řetězec pro oddělení hlavičky od dat.
    """
    if pojistenci:
        print("Seznam pojištěnců:")
        print(hlavicka)
        print(dekorator)
        for osoba in pojistenci:
            print(osoba)
    else:
        print("Žádný pojištěnec nebyl nalezen.")