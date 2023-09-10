from sympy.ntheory.residue_ntheory import primitive_root


def main():
    p = 1234567890123456789012345678901234567890123456789012345678901234567890123459287
    # q = 617283945061728394506172839450617283945061728394506172839450617283945061729643
    proot = primitive_root(p)
    print(f"The smallest primitive root modulo p is: {proot}")


if __name__ == "__main__":
    main()
