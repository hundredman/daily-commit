# https://www.acmicpc.net/problem/1260
# DFS와 BFS를 구현하는 문제

import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
result_dfs = []

def dfs(node):
    visited_dfs[node] = True
    result_dfs.append(node)
    for neighbor in graph[node]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

visited_bfs = [False] * (n + 1)
result_bfs = []

def bfs(start_node):
    queue = deque([start_node])
    visited_bfs[start_node] = True
    while queue:
        current_node = queue.popleft()
        result_bfs.append(current_node)
        for neighbor in graph[current_node]:
            if not visited_bfs[neighbor]:
                queue.append(neighbor)
                visited_bfs[neighbor] = True

dfs(v)
bfs(v)

print(*result_dfs)
print(*result_bfs)