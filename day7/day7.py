import numpy as np

crabs = np.array([int(x) for x in input().split(",")])

min_fuel_pt1, min_fuel_pt2 = float("inf"), float("inf")

for final_pos in range(crabs.max()):
    n_steps = np.abs(crabs[crabs != final_pos] - final_pos)
    fuel1, fuel2 = n_steps.sum(), (n_steps*(n_steps+1) / 2).sum()

    min_fuel_pt1 = min(min_fuel_pt1, fuel1)
    min_fuel_pt2 = min(min_fuel_pt2, fuel2)

print(min_fuel_pt1, "\n", int(min_fuel_pt2))
