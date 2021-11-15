from math import gcd

N = 6
TESTS = (8, 5, 10, 6, 7)


def pseudo_prime_test(a: int) -> bool:
    # N cannot be composite
    return not (gcd(a, N) != 1 or pow(a, N - 1, N) != 1)


for a in TESTS:
    if pseudo_prime_test(a):
        print(a)
