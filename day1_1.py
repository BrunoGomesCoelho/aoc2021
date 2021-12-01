current = None
counter = 0

while (inp := input()):
    inp = int(inp)
    if current is not None and inp > current:
        counter += 1
    current = inp

print(counter)
