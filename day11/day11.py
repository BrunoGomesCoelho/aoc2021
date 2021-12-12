import numpy as np

THRESHOLD = 10


def get_neighbours(energies, i, j):
    return ((i-1,j-1), (i-1, j), (i-1, j+1),
            (i,j-1),             (i, j+1),
            (i+1,j-1), (i+1, j), (i+1, j+1))


energies = np.genfromtxt("input.txt", delimiter=1)
original_size = len(energies)
energies = np.pad(energies, pad_width=1, mode="constant", constant_values=float("-inf"))

step, flash_count = 1, 0

while True:
    energies += 1

    flashed = np.full((original_size+2, original_size+2), False)  # +2 bcs padding
    to_flash = np.transpose(np.nonzero(energies >= THRESHOLD)).tolist()

    while to_flash:
        i, j = to_flash.pop()
        flashed[i, j] = True

        for x, y in get_neighbours(energies, i, j):
            energies[x, y] += 1

            if (energies[x, y] >= THRESHOLD and not flashed[x, y]
                and [x, y] not in to_flash):
                to_flash.append([x, y])

    flash_count += flashed.sum()

    if step == 100:
        print("Part 1", flash_count)

    if flashed.sum() == original_size**2:
        print("Part 2", step)
        break  # assuming this always ends later than part 1

    energies[energies >= THRESHOLD] = 0
    step += 1
