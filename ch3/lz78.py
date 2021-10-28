import re


def encode(decoded: str) -> str:
    ans: str = ""
    prefixes: list[str] = []  # seen prefixes

    left = 0
    while left < len(decoded):
        # try to find the largest prefix
        largest_prefix = ""
        right = len(decoded)
        while left <= right:
            if (largest_prefix := decoded[left:right] or "") in prefixes:
                # largest prefix found
                new_char = decoded[right]
                largest_prefix_index = prefixes.index(largest_prefix) + 1  # 1-indexed
                left = right + 1
                break
            right -= 1
        else:
            # prefix not found
            new_char = decoded[left]
            largest_prefix_index = 0
            left += 1

        # update lists
        prefixes.append(largest_prefix + new_char)
        ans += f"({largest_prefix_index},{new_char})"

    return ans


def decode(encoded: str) -> str:
    # convert to list
    groupings = re.findall(r"(?<=\()(.*?)(?=\))", encoded)
    groupings = [(int(x[0]), x[1]) for group in groupings if (x := group.split(","))]

    # dictionary lookup
    lookup = [""]
    for prefix_index, suffix in groupings:
        lookup.append(lookup[prefix_index] + suffix)

    return "".join(lookup)


if __name__ == "__main__":
    # print(decode("(0,b)(0,a)(1,c)(3,a)(3,b)(5,a)"))
    print(decode("(0,c)(0,b)(1,a)(2,a)(4,a)(5,b)"))
    # print(encode("abbcbcababcaa"))
    # print(encode("bbabacbacbbacbbbacbc"))
    pass
