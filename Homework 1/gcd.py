def gcd(a: int, b: int):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    a = 1234567890123456789012345678901234567890123456789012345678901234567890123456789
    b = 234567890123456789012345678901234567890123456789012345678901234567890123456789

    print("gcd(a,b) =", gcd(a, b))


if __name__ == "__main__":
    main()
