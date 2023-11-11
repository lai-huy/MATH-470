from numpy import gcd
from typing import Callable


def pollard_rho(n: int, seed: int = 2, f: Callable[[int], int] = lambda x: x * x + 1) -> int:
    x, y = seed, seed
    d = 0
    while (not (1 < d < n)):
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd(x - y, n)
    return d


def main():
    nums = [2201, 9409613, 1782886219]

    for N in nums:
        factor = pollard_rho(N, 0, lambda x: x * x + 1)
        other_factor = N // factor
        print(f"{factor}/sqrt({N}) = {factor * pow(N, -0.5)}")
        print(f"{N} = {factor} * {other_factor}")


if __name__ == "__main__":
    main()
