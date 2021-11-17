MOD = 13
ORD = 6
# find a
a = 1
while True:
    if pow(a, ORD, MOD) == 1:
        print(a)
        break
    a += 1

# find other primitive elements
from math import gcd

print("Primitive Elements")
FIELD_SIZE = 27
PRIMITIVE_ELEMENT = 2

ans = set()
for k in range(1, FIELD_SIZE):
    if gcd(k, FIELD_SIZE - 1) == 1:
        ans.add(pow(PRIMITIVE_ELEMENT, k, FIELD_SIZE))
print(ans)
