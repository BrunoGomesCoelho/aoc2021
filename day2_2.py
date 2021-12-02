horizontal = 0
aim = 0
vertical = 0

while (inp := input()):
    direction, value = inp.split()
    value = int(value)
    match direction:
        case "forward":
            horizontal += value
            vertical += aim*value
        case "down":
            aim += value
        case "up":
            aim -= value

print(horizontal*vertical)
