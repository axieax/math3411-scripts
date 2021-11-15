from math import ceil, sqrt

N = 35581
a = ceil(sqrt(N))
while True:
    if N % a == 0:
        print((a, N // a))
        break
    a += 1
