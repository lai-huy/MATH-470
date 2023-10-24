def gcdExtended(a, b):
    if (a == 0):
        return b, 0, 1

    g, v, u = gcdExtended(b % a, a)
    return g, u - (b // a) * v, v


def modInverse(a, m):
    g, u, v = gcdExtended(a, m)
    if (g != 1):
        raise Exception("No Modular Inverse")
    return u % m


def main():
    a = 17
    b = 19079

    aInv = modInverse(a, b)
    bInv = modInverse(b, a)

    print(f"a^(-1) mod b = {aInv}")
    print(f"a*a^(-1)==1 mod b? {(a * aInv) % b == 1}")

    print(f"b^(-1) mod a = {bInv}")
    print(f"b*b^(-1)==1 mod a? {(b * bInv) % a == 1}")


if __name__ == "__main__":
    main()
