"""Input"""
ISBN = "1-698-40364-X"
CHECK_DIGIT = 9

"""Constants"""
NUM_DIGITS = 11
X = 10

"""Calculate Syndrome without CHECK_DIGIT"""
ISBN_DIGITS = [int(digit) if digit.isdigit() else X for digit in ISBN.replace("-", "")]
syndrome = sum(
    (X - index) * value  # digit * value
    for index, value in enumerate(ISBN_DIGITS)  # iterate over digits
    if index != CHECK_DIGIT - 1  # ignore CHECK_DIGIT
)

"""Find Correction to Make Syndrome Divisible by NUM_DIGITS"""
correction = 0
while (syndrome + correction * (NUM_DIGITS - CHECK_DIGIT)) % NUM_DIGITS != 0:
    correction += 1
print(correction)
