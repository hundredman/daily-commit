# https://www.acmicpc.net/problem/15649
# N과 M (1) - Backtracking

import sys

n, m = map(int, sys.stdin.readline().split())

s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i + 1)
        s.pop()

dfs(1)