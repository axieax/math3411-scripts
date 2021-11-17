from math import gcd
from random import randint

N = 25
TESTS = (4, 5, 2, 3)
STRONG = False


def pseudo_prime_test(a: int) -> bool:
    # N cannot be composite
    return not (gcd(a, N) != 1 or pow(a, N - 1, N) != 1)


# strong pseudo prime test adapted from https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/


# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miller_rabin_test(d: int, a: int) -> bool:
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + randint(1, N - 4)

    # Compute a^d % n
    x = pow(a, d, N)

    if x == 1 or x == N - 1:
        return True

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while d != N - 1:
        x = pow(x, x, N)
        d *= 2

        if x == 1:
            return False
        if x == N - 1:
            return True

    # Return composite
    return False


# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def strong_pseudo_prime_test(a: int) -> bool:
    # Corner cases
    if N <= 1 or N == 4:
        return False
    if N <= 3:
        return True

    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = N - 1
    while d % 2 == 0:
        d //= 2

    # Iterate given number of 'k' times
    for _ in range(1000):
        if miller_rabin_test(d, a) == False:
            return False

    return True


for a in TESTS:
    if not STRONG and pseudo_prime_test(a):
        print(a)
    elif STRONG and strong_pseudo_prime_test(a):
        print(a)
