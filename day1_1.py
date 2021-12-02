current = float('-inf')
counter = 0

while (inp := input()):
    inp = int(inp)
    if inp > current:
        counter += 1
    current = inp

print(counter)
