import re
from collections import Counter, defaultdict

recipes = {}
pair_counts = defaultdict(int)

template = input()
for a, b in zip(template[:-1], template[1:]):
    pair_counts[a+b] += 1
input()  # fuck you gabriel

while inp := input():
    [(adjacent, newchar)] = re.findall("([A-Z]+) -> ([A-Z])", inp)
    recipes[adjacent] = newchar

for _ in range(40):
    for (a, b), count in pair_counts.copy().items():
        if a+b in recipes:
            new_letter = recipes[a+b]

            pair_counts[a+b] -= count  # remove the pair that was split
            pair_counts[a+new_letter] += count
            pair_counts[new_letter+b] += count

letter_counts = defaultdict(int)
for pair, pair_count in pair_counts.items():
    for letter in pair:
        letter_counts[letter] += pair_count

# all letters are counted twice except for the first and last
letter_counts[template[0]] += 1
letter_counts[template[-1]] += 1

counts = letter_counts.values()
assert all(v % 2 == 0 for v in counts)
print((max(counts)-min(counts)) // 2)  # undo count twice
