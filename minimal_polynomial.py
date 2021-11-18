# linear combination
FIELD_SIZE = 3
# FIELD_SIZE = 2
Q = (1, 1, 2)
# Q = (1, 0, 0, 1, 1)
HIGHEST_DEGREE = len(Q) - 1

# TODO: linear comb highest

lookup = []
# add basics
for x in range(HIGHEST_DEGREE):
    lookup.append(
        tuple(1 if HIGHEST_DEGREE - i - 1 == x else 0 for i in range(HIGHEST_DEGREE))
    )

# rearrange highest degree term
new = tuple(-q % FIELD_SIZE for q in Q)
lookup.append(new[1:])

# remaining
a = HIGHEST_DEGREE + 1
while True:
    # move along
    prev = lookup[a - 1]
    shifted = prev[1:] + (0,)
    maxx = prev[0]
    if maxx != 0:
        extra = tuple(maxx * q % FIELD_SIZE for q in lookup[HIGHEST_DEGREE])
        shifted = tuple(sum(t) % FIELD_SIZE for t in zip(shifted, extra))
    lookup.append(shifted)
    if all(q == 0 for q in shifted[:-1]) and shifted[-1] == 1:
        break
    a += 1

print(f"{lookup=}")

LOOP = len(lookup) - 1
print(f"{LOOP=}")

### minimal polynomial for POWER
from itertools import combinations

POWER = 3
# POWER = 14

# find recurring powers
degrees = {POWER}
x = POWER
while True:
    x = x * FIELD_SIZE % LOOP
    if x in degrees:
        break
    degrees.add(x)
print(f"{degrees=}")

print("Term\tCoefficient\n--\t--")
for i in range(HIGHEST_DEGREE + 1):
    combs = combinations(degrees, i)
    # print(list(combs))
    o = [sum(t) % LOOP for t in combs]
    lookup_map = [lookup[x] for x in o]
    ans = [
        sum(t) % FIELD_SIZE if i % 2 == 0 else -sum(t) % FIELD_SIZE
        for t in zip(*lookup_map)
    ]
    # print(ans)
    x_pow = HIGHEST_DEGREE - i
    output = f"x^{x_pow}\t{ans}"
    print(output)
