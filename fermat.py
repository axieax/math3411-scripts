from math import ceil, sqrt

N = 24871

a = ceil(sqrt(N))
while True:
    if N % a == 0:
        b = N // a
        print((a, b))
        print(f"b - a = {abs(b - a)}")
        break
    a += 1
