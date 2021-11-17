from math import log

RADIX = 2

M = [
    [0.25, 0.5],
    [0.75, 0.5],
]
M_TRANSFORM = [list(x) for x in zip(*M)]

P = [
    0.4,
    0.6,
]


def calc(m):
    return -m * log(m, RADIX)


ans = 0
for M_COL, P_ROW in zip(M_TRANSFORM, P):
    for m in M_COL:
        ans += P_ROW * calc(m)
print(ans)
