"""Checks if a set of codewords is uniquely decodable"""
from itertools import permutations

c = ["10", "11", "100"]
options = ["1", "111", "011", "0"]
# c = ["10", "11", "01"]
# options = ["1001", "1000", "0001", "1100"]
# c = ["1", "10", "01"]
# options = ["2", "3", "4", "5"]
# c = ["00", "10", "1100"]
# options = ["111", "1011", "1010", "0000"]
# c = ["", "", ""]
# options = ["", "", "", ""]

for option in options:
    check = c + [option]
    arrangements = permutations(check, r=2)
    # uniquely decodeable - not a prefix for other codes
    # NOTE: may not necessarily be true - e.g. 11b and 11 is fine if only b follows
    status = all(not pair[0].startswith(pair[1]) for pair in arrangements)
    if status:
        print(option)
        break
else:
    print(None)
