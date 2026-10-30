def rozsireny_euklides(a, b):
    if a < 0 or b < 0 or (a == 0 and b == 0):
        raise ValueError("Zadej nezáporná čísla, alespoň jedno musí být kladné.")

    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b != 0:
        podil = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - podil * x1
        y0, y1 = y1, y0 - podil * y1

    # Platí původní_a * x0 + původní_b * y0 = NSD.
    return a, x0, y0


if __name__ == "__main__":
    try:
        a = int(input("Zadej a: "))
        b = int(input("Zadej b: "))
        nsd, x, y = rozsireny_euklides(a, b)
        print("Největší společný dělitel:", nsd)
        print("Koeficienty: x =", x, ", y =", y)
        print(f"Bézoutova rovnost: {a} * ({x}) + {b} * ({y}) = {nsd}")
    except ValueError as chyba:
        print("Chyba:", chyba)
