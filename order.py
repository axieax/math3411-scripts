# ord_m(a)
M = 13
A = 6

i = 1
while True:
    if pow(A, i, M) == 1:
        print(i)
        break
    i += 1
