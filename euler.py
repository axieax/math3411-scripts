from math import gcd

M = 361


def phi(m):
    return sum(gcd(x, m) == 1 for x in range(1, m))


print(phi(M))
