from numpy import gcd
from sympy import factorint

def order(a: int, p: int) -> int:
    if gcd(a, p) != 1:
        print("p and b are not co-prime.\n")
        return -1

    for k in range(3, p):
        if (pow(a, k, p) == 1):
            return k
    return -1


def log2(n: int) -> int:
    Q = n
    k = 0
    while not (Q & 1):
        Q >>= 1
        k += 1
    return Q, k


def nonResidue(p: int) -> int:
    for q in range(2, p):
        if pow(q, (p - 1) >> 1, p) == p - 1:
            return q
    return 2


# def TonelliShanks(N, p):
#     if gcd(N, p) != 1:
#         raise ValueError(f"{N} and {p} are not coprime")
#     if pow(N, (p - 1) >> 1, p) == p - 1:
#         raise ValueError(f"{N} does not have a square root modulo {p}")
#     Q, k = log2(p - 1)
#     z = nonResidue(p)

#     # Initializing variable x, b and g
#     x = pow(N, (Q + 1) / 2, p)
#     b = pow(N, Q, p)
#     g = pow(z, Q, p)

#     # keep looping until b become
#     # 1 or m becomes 0
#     while (True):
#         m = 0
#         while (m < k):
#             if (order(p, b) == -1):
#                 return -1

#             # finding m such that b^ (2^m) = 1
#             if (order(p, b) == (1 << m)):
#                 break
#             m += 1

#         if (m == 0):
#             return x

#         # updating value of x, g and b
#         # according to algorithm
#         x = (x * pow(g, 1 << (k - m - 1), p)) % p
#         g = pow(g, 1 << (k - m), p)
#         b = (b * g) % p

#         if (b == 1):
#             return x
#         k = m

def TonelliShanks(a, p):
    z = nonResidue(p - 1)
    Q, k = log2(p - 1)
    if pow(a, Q, p) == 1:
        return pow(a, (Q + 1) >> 1, p)
    
    for i in range(0, k - 1):
        if pow(a, Q << i, p) == p - 1:
            b = a * pow(z, 1 << (k - i - 1), p)
            R = TonelliShanks(b)
            return R * z ** -(1 << (k - i - 2))



def main():
    N20 = 35437391370189380023
    # 3680798371 * 9627637213
    
    N30 = 403903264686388453744794079313
    # 525825865925917 * 768131221493189
    
    N40 = 6754910601769419708731690214821789355427
    # 79599963126718408889 * 84860725262095958843
    
    N50 = 60529141009038413034423166889017301527837910258131
    # 6629969174350950380233123 * 9129626310059577844052497
    
    N60 = 133523995803370205942225812853710227025177081936429644652483
    # 192985676104654302319629235559 * 691885524866422775606827175237
    
    N70 = 3426473875287793756703750981622962137419589116424756456135570641437827
    print(factorint(N20))
    print(factorint(N30))
    print(factorint(N40))
    print(factorint(N50))
    print(factorint(N60))
    print(factorint(N70))
    
    e = 65537
    c = 2400556132229818489305649515346654848298483477334619666591280284126769


if __name__ == "__main__":
    main()
