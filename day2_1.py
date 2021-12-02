horizontal = 0
vertical = 0

while (inp := input()):
    direction, value = inp.split()
    value = int(value)
    match direction:
        case "forward":
            horizontal += value
        case "down":
            vertical += value
        case "up":
            vertical -= value

print(horizontal*vertical)
