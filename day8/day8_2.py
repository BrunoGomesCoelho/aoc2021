from collections import defaultdict


def create_mapping(sizes_dict):
    num_to_code = {
        1: sizes_dict[2][0], 7: sizes_dict[3][0], 4: sizes_dict[4][0],
        8: sizes_dict[7][0],
    }

    # 4 - sizes[6] = 9 (if len == 2)
    num_to_code[9] = [x for x in sizes_dict[6]
                        if len(set(x) - set(num_to_code[4])) == 2][0]
    sizes_dict[6].remove(num_to_code[9])

    # sizes[5] - 9 = 2 (if len != 0)
    num_to_code[2] = [x for x in sizes_dict[5]
                        if set(x) - set(num_to_code[9])][0]
    sizes_dict[5].remove(num_to_code[2])

    # if 7 notin sizes[5], we have 5, otherwise 3
    a, b = sizes_dict[5]
    num_to_code[3], num_to_code[5] = (b, a) if set(num_to_code[7]) - set(a) \
                                            else (a, b)

    # if 7 not in sizes[6], we have 6, otherwise 0
    a, b = sizes_dict[6]
    num_to_code[0], num_to_code[6] = (b, a) if set(num_to_code[7]) - set(a) \
                                            else (a, b)

    return {y:str(x) for x, y in num_to_code.items()}


count = 0
while (inp := input()):
    nums, out = [["".join(sorted(x)) for x in y.strip().split(" ")]
                 for y in inp.split("|")]

    sizes_dict = defaultdict(list)  # len(x): [x1, x2, ...]  s.t. len(xi) = len(x)
    for x in nums:
        sizes_dict[len(x)].append(x)

    mapping = create_mapping(sizes_dict)
    count += int("".join(mapping[x] for x in out))

print(count)
