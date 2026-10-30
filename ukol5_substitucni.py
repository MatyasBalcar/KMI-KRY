from pomocne import ABECEDA, je_pismeno, nacti_volbu, preved_text


def over_klic(klic):
    if len(klic) != 26 or not all(je_pismeno(znak) for znak in klic):
        raise ValueError("Klíč musí obsahovat právě 26 písmen A-Z.")
    klic = klic.upper()
    if len(set(klic)) != 26:
        raise ValueError("Každé písmeno musí být v klíči právě jednou.")
    return klic


def zasifruj(text, klic):
    return preved_text(text, over_klic(klic))


def desifruj(text, klic):
    klic = over_klic(klic)
    nova_abeceda = ""
    for znak in ABECEDA:
        nova_abeceda += ABECEDA[klic.index(znak)]
    return preved_text(text, nova_abeceda)


if __name__ == "__main__":
    try:
        volba = nacti_volbu()
        text = input("Zadej text: ")
        klic = input("Zadej přeházenou abecedu (26 různých písmen A-Z): ")
        if volba == "s":
            print(zasifruj(text, klic))
        else:
            print(desifruj(text, klic))
    except ValueError as chyba:
        print("Chyba:", chyba)
