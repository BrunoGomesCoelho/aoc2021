points_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
close_symb_map = {"]": "[", ")": "(", "}": "{", ">": "<"}

illegal = []

while inp := input():
    stack = []
    for c in inp:
        if c not in close_symb_map.keys():
            stack.append(c)
        elif not stack or stack[-1] != close_symb_map[c]:
            illegal.append(c)
            break
        else:
            stack.pop()

print(sum(points_map[x] for x in illegal))


