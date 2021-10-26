"""Input"""
ISBN = "1-698-40364-X".replace("-", "")
CHECK_DIGIT = 9

"""Constants"""
NUM_DIGITS = 10

"""Calculate Syndrome without CHECK_DIGIT"""
ISBN_DIGITS = [int(digit) if digit.isdigit() else NUM_DIGITS for digit in ISBN]
syndrome = sum(
    value * (NUM_DIGITS - index)  # value * digit
    for index, value in enumerate(ISBN_DIGITS)  # iterate over digits
    if index != CHECK_DIGIT - 1  # ignore CHECK_DIGIT
)

"""Error Correcting"""
correction = 0
while (syndrome + correction * (NUM_DIGITS - CHECK_DIGIT + 1)) % (NUM_DIGITS + 1) != 0:
    correction += 1
print(correction)
