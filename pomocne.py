ABECEDA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def je_pismeno(znak):
    return "A" <= znak <= "Z" or "a" <= znak <= "z"


def jen_pismena(text):
    return "".join(znak.upper() for znak in text if je_pismeno(znak))


def preved_text(text, nova_abeceda):
    # Písmeno na pozici i nahradíme písmenem na stejné pozici v nové abecedě.
    vysledek = ""
    for znak in text:
        if je_pismeno(znak):
            pozice = ABECEDA.index(znak.upper())
            novy_znak = nova_abeceda[pozice]
            if znak.islower():
                novy_znak = novy_znak.lower()
            vysledek += novy_znak
        else:
            vysledek += znak
    return vysledek


def nacti_volbu():
    volba = input("Šifrovat (s), nebo dešifrovat (d)? ").strip().lower()
    if volba not in ("s", "d"):
        raise ValueError("Zadej s nebo d.")
    return volba
