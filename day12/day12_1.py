from sys import stdin
from collections import defaultdict

START, END = "start", "end"

def dfs(visited, cur):
    if cur == END:
        return 1

    if not cur.isupper():
        visited[cur] = True
    count = sum(dfs(visited, node) for node in graph[cur] if not visited[node])

    visited[cur] = False
    return count


graph = defaultdict(list)
for a, b in [line.strip().split("-") for line in stdin]:
    graph[a].append(b)
    graph[b].append(a)

visited = defaultdict(bool)
print(dfs(visited, START))
