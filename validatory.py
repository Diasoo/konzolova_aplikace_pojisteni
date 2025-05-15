def zadej_beznou_hodnotu(vstup, pole="hodnota"):
    """
    Funkce pro kontrolu, že vstup není prázdný.
    """
    if vstup.strip() == "":
        print(f"{pole.capitalize()} nesmí být prázdný.")
        return False
    return True

def zadej_vek(vek):
    """
    Funkce pro validaci věku.
    """
    if int(vek) < 1 or int(vek) > 120:
        print("Věk musí být celé číslo mezi 1 a 120.")
        return False
    return True

def zadej_telefon(telefon):
    """
    Funkce pro validaci telefonního čísla.
    """
    if len(telefon) < 9 or len(telefon) > 15:
        print("Telefonní číslo musí mít mezi 9 a 15 znaky.")
        return False
    return True