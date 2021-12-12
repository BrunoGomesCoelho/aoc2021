points_map = {")": 1, "]": 2, "}": 3, ">": 4}
close_symb_map = {"]": "[", ")": "(", "}": "{", ">": "<"}
open_symb_map = {v:k for k,v in close_symb_map.items()}

stacks = []
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
        stacks.append(stack)

scores = []
for stack in stacks:
    score = 0
    while stack:
        c = stack.pop()
        score *= 5
        score += points_map[open_symb_map[c]]
    scores.append(score)

scores = sorted(scores)
print(scores[len(scores)//2])
