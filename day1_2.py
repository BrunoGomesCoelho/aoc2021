first_iter_flag = True

numbers = []
while (inp := input()):
    numbers.append(int(inp))

previous_sum = None
result_count = 0

for a, b, c in zip(numbers, numbers[1:], numbers[2:]):
    new_sum = a+b+c
    if previous_sum is not None and new_sum > previous_sum:
        result_count += 1
    previous_sum = new_sum

print(result_count)
