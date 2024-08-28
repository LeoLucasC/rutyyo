n = int(input("COLOCA EL NUMERO: "))

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


resultado = es_primo(n)


if resultado:
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")


