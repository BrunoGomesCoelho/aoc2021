import numpy as np

NEW_TIMER, NEW_LANT, DAYS = 6, 8, 80  # part1
NEW_TIMER, NEW_LANT, DAYS = 6, 8, 256  # part2

ages = np.zeros(NEW_LANT+1)
for num in [int(x) for x in input().split(",")]:
    ages[num] += 1

for _ in range(DAYS):
    new_ages = np.zeros(NEW_LANT+1)

    # special case: day 0 has a different timer
    new_ages[NEW_TIMER] = ages[0]

    for age in range(NEW_LANT+1):
        new_ages[age-1] += ages[age]
    ages = new_ages

print(int(ages.sum()))
