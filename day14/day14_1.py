import re
from collections import Counter, defaultdict

polymer = input()
input() # fuck you bruno

recipes = defaultdict(str)
while recipe := input():
    [(adjacent, newchar)] = re.findall("([A-Z]+) -> ([A-Z])", recipe)
    recipes[adjacent] = newchar

for _ in range(10):
    new_polymer = [a + recipes[a+b] for a, b in zip(polymer, polymer[1:])]
    polymer = "".join(new_polymer) + polymer[-1]

(_, most), *_, (_, least) = Counter(polymer).most_common()
print(most-least)

