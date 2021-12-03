# counter = [0]*5
counter = [0]*12

while (inp := input()):
    for idx, char in enumerate(inp):
        match char:
            case "1":
                counter[idx] += 1
            case "0":
                counter[idx] -= 1
            case _:
                print(f"Huh? '{char}'")

# not sure when there's a tie, counting it as a 1
gamma = int("".join([str(int(x >= 0)) for x in counter]), 2)
epsilon = int("".join([str(int(x < 0)) for x in counter]), 2)
print(gamma*epsilon)
