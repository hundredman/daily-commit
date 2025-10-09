# https://www.acmicpc.net/problem/15651
# N과 M (3) - Backtracking with Repetition

import sys

n, m = map(int, sys.stdin.readline().split())

s = []

def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()

dfs()