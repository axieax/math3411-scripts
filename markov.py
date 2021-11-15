R = 3
P = 0.63
l = 1
while True:
    LHS = 1 / P
    RHS = R / P
    if LHS <= R ** l < RHS:
        print(l)
        break
