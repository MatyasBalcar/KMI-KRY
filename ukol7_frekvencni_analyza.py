from pomocne import ABECEDA, jen_pismena


def frekvencni_analyza(text, delka=1):
    if delka not in (1, 2, 3):
        raise ValueError("Délka skupiny musí být 1, 2 nebo 3.")

    text = jen_pismena(text)
    pocty = {}
    if delka == 1:
        for znak in ABECEDA:
            pocty[znak] = 0

    # Skupiny se překrývají, např. ABABA obsahuje ABA dvakrát.
    for i in range(len(text) - delka + 1):
        skupina = text[i:i + delka]
        pocty[skupina] = pocty.get(skupina, 0) + 1
    return pocty


def vypis_frekvence(text, delka=1):
    pocty = frekvencni_analyza(text, delka)
    celkem = sum(pocty.values())
    if not pocty:
        print("Žádné výskyty.")
        return

    for skupina in sorted(pocty):
        pocet = pocty[skupina]
        podil = 100 * pocet / celkem if celkem else 0
        print(f"{skupina}: {pocet} ({podil:.2f} %)")


if __name__ == "__main__":
    try:
        volba = input("Vstup z textu (t), nebo ze souboru (s)? ").strip().lower()
        if volba == "t":
            text = input("Zadej text: ")
        elif volba == "s":
            cesta = input("Cesta k textovému souboru: ").strip().strip('"')
            with open(cesta, encoding="utf-8-sig") as soubor:
                text = soubor.read()
        else:
            raise ValueError("Zadej t nebo s.")

        print("\nPísmena:")
        vypis_frekvence(text)
        print("\nDvojice (digramy):")
        vypis_frekvence(text, 2)
        print("\nTrojice (trigramy):")
        vypis_frekvence(text, 3)
    except (ValueError, OSError) as chyba:
        print("Chyba:", chyba)
