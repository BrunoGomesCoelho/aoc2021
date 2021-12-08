count = 0
valid_sizes = [2, 3, 4, 7]
while (inp := input()):
    for word_size in map(len, inp.split("|")[1].split(" ")):
        if word_size in valid_sizes:
            count += 1
    print(count)
