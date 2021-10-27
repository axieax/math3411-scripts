def decode(
    partitions: list[tuple[float, float]], symbols: list[str], encoded: float
) -> list[str]:
    ans = []
    curr = encoded
    partition_index = -1

    # loop until stopword decoded
    while not ans or (ans[-1] != symbols[-1]):
        # ignore calculation for first time
        if partition_index != -1:
            lower_bound, upper_bound = partitions[partition_index]
            interval_length = upper_bound - lower_bound
            curr = (curr - lower_bound) / interval_length

        # find new partition
        partition_index = [
            i for i, tup in enumerate(partitions) if tup[0] <= curr < tup[1]
        ][0]

        # decode symbol
        ans.append(symbols[partition_index])

    print(*ans)
    return ans


def encode(
    partitions: list[tuple[float, float]], symbols: list[str], decoded: list[str]
) -> None:
    interval_lower = 0
    interval_upper = 1
    for char in decoded:
        # find new subinterval
        index = symbols.index(char)
        sub_interval_lower, sub_interval_upper = partitions[index]

        # update current interval
        interval_length = interval_upper - interval_lower
        interval_upper = interval_lower + interval_length * sub_interval_upper
        interval_lower += interval_length * sub_interval_lower

    print(f"Choose a random number from [{interval_lower}, {interval_upper})")


if __name__ == "__main__":
    """
    # Examples
    partitions = [(0, 0.2), (0.2, 0.9), (0.9, 1)]
    symbols = ["s1", "s2", "."]
    decode(partitions, symbols, 0.4331)
    partitions = [(0, 0.4), (0.4, 0.7), (0.7, 0.85), (0.85, 1)]
    symbols = ["s1", "s2", "s3", "."]
    encode(partitions, symbols, ["s2", "s1", "s3", "."])
    """
    partitions = [(0, 0.2), (0.2, 0.9), (0.9, 1)]
    symbols = ["s1", "s2", "."]
    # decode(partitions, symbols, 0.4331)
    # encode(partitions, symbols, ["s1", "s2", "."])
    pass
