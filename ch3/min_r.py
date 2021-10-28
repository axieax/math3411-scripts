lengths = [1, 2, 2, 3, 3, 3]
for r in range(1, 4):
    if sum(1 / (r ** length) for length in lengths) <= 1:
        print(r)
        break
