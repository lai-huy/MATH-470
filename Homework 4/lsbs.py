from math import ceil, sqrt


def fast_pow(base: int, power: int, modulo: int) -> int:
    result = 1
    base %= modulo

    while power > 0:
        if power & 1:
            result = (result * base) % modulo
        base = (base * base) % modulo
        power >>= 1

    return result


def lsbs(g: int, h: int, p: int) -> int:
    N = ceil(sqrt(p - 1))

    # Little Step
    little = {fast_pow(g, i, p): i for i in range(N + 1)}

    # Use Fermat's Little Theorem to Calculate g^{-n}
    g_inv = fast_pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * fast_pow(g_inv, j, p)) % p
        print(f"Checking {y}")
        if y in little:
            return j * N + little[y]

    # Solution not found
    return None


def main():
    p = 19079
    h = 19
    g = 17
    print(f"{g}^{lsbs(g, h, p)}=={h} mod {p}")


if __name__ == "__main__":
    main()
