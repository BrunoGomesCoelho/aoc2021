def calc_score(stack):
    score = 0
    while stack:
        c = stack.pop()
        score = score*5 + points_map[open_symb_map[c]]

    return score


scores = []
points_map = {")": 1, "]": 2, "}": 3, ">": 4}
close_symb_map = {"]": "[", ")": "(", "}": "{", ">": "<"}
open_symb_map = {v:k for k,v in close_symb_map.items()}

while inp := input():
    stack = []
    for c in inp:
        if c not in close_symb_map.keys():
            stack.append(c)
        elif not stack or stack[-1] != close_symb_map[c]:
            break
        else:
            stack.pop()
    else:
        scores.append(calc_score(stack))

print(sorted(scores)[len(scores)//2])
