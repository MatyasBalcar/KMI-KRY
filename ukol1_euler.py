def eulerova_funkce(n):
    if n < 1:
        raise ValueError("Číslo n musí být alespoň 1.")

    vysledek = n
    delitel = 2
    while delitel * delitel <= n:
        if n % delitel == 0:
            # Za každého prvočíselného dělitele p odečteme výsledek / p.
            vysledek -= vysledek // delitel
            while n % delitel == 0:
                n //= delitel
        delitel += 1

    if n > 1:
        vysledek -= vysledek // n
    return vysledek


if __name__ == "__main__":
    try:
        n = int(input("Zadej přirozené číslo n: "))
        print("Eulerova funkce:", eulerova_funkce(n))
    except ValueError as chyba:
        print("Chyba:", chyba)
