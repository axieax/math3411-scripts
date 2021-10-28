COMMA_LENGTH = 4
SYMBOLS = ["s1", "s2", "s3", "s4", "s5"]
DECODED = ["s2", "s4", "s1", "s5", "s4"]

map = ["0"]
for index, symbol in enumerate(SYMBOLS[1:]):
    map.append("1" + map[index])
if COMMA_LENGTH < len(SYMBOLS):
    map[-1] = map[-1][:-1]
# print(map)

# encode
for d in DECODED:
    print(map[SYMBOLS.index(d)], end="")
print()
