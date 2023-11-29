from math import inf, isinf
from numpy import gcd


class Curve:
    a: int
    b: int
    N: int

    def __init__(self, a: int, b: int, N: int):
        assert (4 * a * a * a + 27 * b * b) % N, "Degenerate elliptic curve"
        self.a = a % N
        self.b = b % N
        self.N = N

    def __str__(self) -> str:
        return f"y^2 = x^3 + {self.a}x + {self.b}"

    def __contains__(self, point: "Point") -> bool:
        x, y = point.x, point.y
        return pow(y, 2, self.N) == (x * x * x + self.a * x + self.b) % self.N

    def __eq__(self, other: "Curve") -> bool:
        if not isinstance(other, Curve):
            return False
        if self.N != other.N:
            return False
        return self.a == other.a and self.b == other.b


class Point:
    x: int
    y: int
    curve: Curve

    I: "Point" = None

    def __init__(self, x: float, y: float, curve: Curve):
        self.x = x % curve.N if not isinf(x) else inf
        self.y = y % curve.N if not isinf(x) else inf
        self.curve = curve

    def __str__(self) -> str:
        if isinf(self.x) and isinf(self.y):
            return "$\mathcal{O}$"
        return f"$({self.x}, {self.y})$"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return False

        if isinf(self.x) ^ isinf(other.x):
            return False
        if isinf(self.x) and isinf(other.x):
            return True

        if self.curve.N != other.curve.N:
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Point") -> "Point":
        if self == Point.I:
            return other

        if other == Point.I:
            return self

        if self.x == other.x and not ((self.y + other.y) % self.curve.N):
            return Point.I

        if self.x != other.x:
            x1, y1 = self.x, self.y
            x2, y2 = other.x, other.y

            m: int = ((y2 - y1) * pow(x2 - x1, -1,
                      self.curve.N)) % self.curve.N
            x3: int = (m * m - x1 - x2) % self.curve.N
            y3: int = (m * (x1 - x3) - y1) % self.curve.N

            return Point(x3, y3, self.curve)

        else:
            x1, y1, a = self.x, self.y, self.curve.a

            m: int = ((3 * x1 * x1 + a) * pow(y1 << 1, -
                      1, self.curve.N)) % self.curve.N
            x3: int = (m * m - (x1 << 1)) % self.curve.N
            y3: int = (m * (x1 - x3) - y1) % self.curve.N

            return Point(x3, y3, self.curve)

    def __rmul__(self, scalar: int) -> "Point":
        current = self
        result = Point.I
        while scalar:
            if scalar & 1:
                result = result + current
            current = current + current
            scalar >>= 1
        return result


def main():
    Point.I = Point(inf, inf, None)
    a, b, N = 4, 128, 26167
    curve = Curve(a, b, N)
    P = Point(2, 12, curve)
    Q = 6 * 5 * 4 * 3 * 2 * 1 * P
    A = 3 * Q
    B = 4 * Q
    g = gcd((B.x - A.x) % Q.curve.N, Q.curve.N)
    print(g, N // g)
    return


if __name__ == "__main__":
    main()
