# from sympy.ntheory.residue_ntheory import primitive_root
from math import sqrt
from typing import List, Set


def fast_pow(base, power, modulo):
    result = 1
    base %= modulo

    while power > 0:
        if power & 1:
            result = (result * base) % modulo
        base = (base * base) % modulo
        power >>= 1

    return result


def is_primitive_root(g: int, p: int) -> bool:
    # Factors were found using Wolfram Alpha
    # https://www.wolframalpha.com/input?i=Factors+of+%5B%2F%2Fquantity%3A1234567890123456789012345678901234567890123456789012345678901234567890123459286%2F%2F%5D
    factors = [
        2, 617283945061728394506172839450617283945061728394506172839450617283945061729643]
    for q in factors:
        if (fast_pow(g, (p - 1) // q, p) == 1):
            return False
        return True


def primitive_root(p: int) -> int:

    for g in range(2, p):
        print(f"Checking: {g}")
        if (is_primitive_root(g, p)):
            return g

    return -1


def main() -> None:
    p = 1234567890123456789012345678901234567890123456789012345678901234567890123459287
    # q = 617283945061728394506172839450617283945061728394506172839450617283945061729643
    proot = primitive_root(p)
    print(f"The smallest primitive root modulo p is: {proot}")


if __name__ == "__main__":
    main()
