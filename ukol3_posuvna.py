from pomocne import ABECEDA, nacti_volbu, preved_text


def zasifruj(text, posun):
    nova_abeceda = ""
    for i in range(26):
        nova_abeceda += ABECEDA[(i + posun) % 26]
    return preved_text(text, nova_abeceda)


def desifruj(text, posun):
    return zasifruj(text, -posun)


if __name__ == "__main__":
    try:
        volba = nacti_volbu()
        text = input("Zadej text: ")
        posun = int(input("Zadej posun: "))
        if volba == "s":
            print(zasifruj(text, posun))
        else:
            print(desifruj(text, posun))
    except ValueError as chyba:
        print("Chyba:", chyba)
