# https://www.acmicpc.net/problem/15652
# N과 M (4) - Combinations with Repetition

import sys

n, m = map(int, sys.stdin.readline().split())

s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)