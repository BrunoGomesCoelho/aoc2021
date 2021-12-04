numbers = []
while (inp := input()):
    numbers.append(int(inp))

previous_sum = float('-inf')
result_count = 0

for a, b, c in zip(numbers, numbers[1:], numbers[2:]):
    new_sum = a+b+c
    if new_sum > previous_sum:
        result_count += 1
    previous_sum = new_sum

print(result_count)
