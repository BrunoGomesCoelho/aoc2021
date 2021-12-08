from collections import defaultdict


def size_isin_left(left, right):
    return len([x for x in left if x not in right])


def create_mapping(sizes_dict):
    num_to_code = {
        1: sizes_dict[2][0], 7: sizes_dict[3][0], 4: sizes_dict[4][0],
        8: sizes_dict[7][0],
    }

    # 4 - sizes[6] = 9 (if len == 1)
    num_to_code[9] = [x for x in sizes_dict[6]
                        if size_isin_left(x, num_to_code[4]) == 2][0]
    sizes_dict[6].remove(num_to_code[9])

    # sizes[5] - 9 = 2 (if len != 0)
    num_to_code[2] = [x for x in sizes_dict[5]
                        if size_isin_left(x, num_to_code[9])][0]
    sizes_dict[5].remove(num_to_code[2])

    # if 7 in sizes[5], = 3, otherwise 5
    for cand_3 in sizes_dict[5]:
        if all(x in cand_3 for x in num_to_code[7]):
            num_to_code[3] = cand_3
        else:
            num_to_code[5] = cand_3

    # if 7 in sizes[6], = 0, otherwise 6
    for cand_3 in sizes_dict[6]:
        if all(x in cand_3 for x in num_to_code[7]):
            num_to_code[0] = cand_3
        else:
            num_to_code[6] = cand_3

    return {y:str(x) for x, y in num_to_code.items()}


count = 0

while (inp := input()):
    nums, out = [["".join(sorted(x)) for x in y.strip().split(" ")]
                 for y in inp.split("|")]

    sizes_dict = defaultdict(list)
    for x in nums:
        sizes_dict[len(x)].append(x)

    mapping = create_mapping(sizes_dict)
    count += int("".join(mapping[x] for x in out))

print(count)
