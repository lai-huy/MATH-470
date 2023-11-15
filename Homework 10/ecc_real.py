from math import inf


class Curve:
    a: int
    b: int

    def __init__(self, a: int, b: int):
        assert (4 * a * a * a) != (-27 * b * b), "Degenerate elliptic curve"
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"y^2 = x^3 + {self.a}x + {self.b}"

    def __contains__(self, point: "Point") -> bool:
        x, y = point.x, point.y
        return y ** 2 == x ** 3 + self.a * x + self.b

    def __eq__(self, other: "Curve") -> bool:
        return self.a == other.a and self.b == other.b if isinstance(other, Curve) else False


class Point:
    x: float
    y: float
    curve: Curve

    I: "Point" = None

    def __init__(self, x: float, y: float, curve: Curve):
        self.x = x
        self.y = y
        self.curve = curve

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve if isinstance(other, Point) else False

    def __add__(self, other: "Point"):
        if self == Point.I:
            return other

        if other == Point.I:
            return self

        if self.x == other.x and self.y == (-1 * other.y):
            return Point.I

        if self.x != other.x:
            x1, y1 = self.x, self.y
            x2, y2 = other.x, other.y

            m: float = (y2 - y1) / (x2 - x1)
            x3: float = m * m - x1 - x2
            y3: float = m * (x1 - x3) - y1

            return Point(x3, y3, self.curve)

        else:
            x1, y1, a = self.x, self.y, self.curve.a

            m: float = (3 * x1 * x1 + a) / (2 * y1)
            x3: float = m * m - (2 * x1)
            y3: float = m * (x1 - x3) - y1

            return Point(x3, y3, self.curve)

    def __sub__(self, other: "Point") -> "Point":
        return self + Point(other.x, -1 * other.y, self.curve)

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
    curve = Curve(0, 17)
    P = Point(-1, 4, curve)
    Q = Point(2, 5, curve)
    print(P + Q)
    print(P - Q)


if __name__ == "__main__":
    main()
