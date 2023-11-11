from numpy import gcd


def pollard(N):
    a, i = 2, 2
    g = 1

    # iterate till a prime factor is obtained
    while (g <= 1):
        a = pow(a, i, N)
        g = gcd(a - 1, N)
        i += 1
    return g


def main():
    N = 340510176929609558738506407941198102081020749940944635553628097992090306553579338501

    factor = pollard(N)
    other_factor = N // factor
    print(f"Factor found: {factor}")
    print(f"Other factor: {other_factor}")


if __name__ == "__main__":
    main()
