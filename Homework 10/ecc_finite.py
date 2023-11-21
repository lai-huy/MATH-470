from math import inf, isinf


class Curve:
    a: int
    b: int
    N: int

    def __init__(self, a: int, b: int, N: int):
        assert (4 * a ** 3 + 27 * b * b) % N, "Degenerate elliptic curve"
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

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.N))


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

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.curve))

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

    def __lt__(self, other: "Point") -> bool:
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y


def legendre(a: int, p: int) -> int:
    return pow(a, (p - 1) >> 1, p)


def tonelli(n: int, p: int) -> int:
    if not n:
        return 0
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while not (q & 1):
        q >>= 1
        s += 1
    if s == 1:
        return pow(n, (p + 1) >> 2, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) >> 1, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p:
        t2 = (t * t) % p
        for i in range(1, m):
            if not ((t2 - 1) % p):
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


def main():
    Point.I = Point(inf, inf, None)
    a, b, N = 2, 5, 11
    curve = Curve(a, b, N)
    qr = set([0])

    # calculate all qr's mod N
    for i in range(curve.N):
        if legendre(i, curve.N) == 1:
            qr.add(i)
    qr = sorted(qr)

    # find the x for all of these roots
    points = set()
    for i in range(N):
        x = (i * i * i + curve.a * i + curve.b) % curve.N
        print(f"i={i}, x={x}")
        if x in qr:
            r = tonelli(x, curve.N)
            points.add(Point(i, r, curve))
            points.add(Point(i, -1 * r % curve.N, curve))
    points = sorted(points)
    points.insert(0, Point.I)

    # the table
    for p1 in points:
        print(f"{p1}", end=" & ")
        for p2 in points:
            print(f"{p1 + p2}", end=" & ")
        print("\\\\ \hline")


if __name__ == "__main__":
    main()
