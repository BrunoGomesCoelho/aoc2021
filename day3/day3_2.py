import numpy as np  # yes I'm using numpy, deal with it

numbers = []
while (inp := input()):
    numbers.append([int(x) for x in inp])

numbers = np.array(numbers)
n_numbers, n_bits = numbers.shape
oxigen_valid = np.full(n_numbers, True)
co2_valid = np.full(n_numbers, True)

for bit in range(n_bits):
    if oxigen_valid.sum() != 1:
        mst_cmn = int(numbers[oxigen_valid, bit].mean() >= 0.5)
        oxigen_valid = np.logical_and(oxigen_valid, numbers[:, bit] == mst_cmn)

    if co2_valid.sum() != 1:
        lst_cmn  = int(numbers[co2_valid, bit].mean() >= 0.5) != 1
        co2_valid = np.logical_and(co2_valid, numbers[:, bit] == lst_cmn)

def convert_bin(array):
    array = array.reshape(-1)
    return array.dot(2**np.arange(array.size)[::-1])

print(convert_bin(numbers[oxigen_valid]) * convert_bin(numbers[co2_valid]))
