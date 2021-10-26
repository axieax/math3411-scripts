"""Input"""
ISBN = "8-511-20778-1"
CHECK_DIGIT = 9

"""Calculation"""
syndrome = 0
isbn_digits = [int(digit) if digit.isdigit() else 10 for digit in ISBN.replace("-", "")]
for index, value in enumerate(isbn_digits):
    # ignore check digit (1-indexed)
    if index == CHECK_DIGIT - 1:
        continue
    digit = 10 - index
    syndrome += digit * value

# find correction
correction = 0
while (syndrome + correction * (10 - CHECK_DIGIT + 1)) % 11 != 0:
    correction += 1

print(correction)
