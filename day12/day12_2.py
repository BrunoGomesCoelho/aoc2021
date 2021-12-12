from sys import stdin
from collections import defaultdict

START, END = "start", "end"

def dfs(visited, cur, visited_twice):
    if cur == END:
        return 1

    if not cur.isupper():
        visited[cur] = True

    count = 0
    for node in graph[cur]:
        if not visited[node]:
            count += dfs(visited, node, visited_twice=visited_twice)
        elif visited_twice is None and node not in (START, END):
            count += dfs(visited, node, visited_twice=node)

    if visited_twice != cur:  # in second visit we don't unmark
        visited[cur] = False
    return count


graph = defaultdict(list)
for a, b in [line.strip().split("-") for line in stdin]:
    graph[a].append(b)
    graph[b].append(a)

visited = defaultdict(bool)
print(dfs(visited, START, visited_twice=None))
