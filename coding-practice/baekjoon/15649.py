# https://www.acmicpc.net/problem/15649
# N과 M (1) - Backtracking

import sys

def backtrack(n, m, path):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(1, n + 1):
        if i not in path:
            path.append(i)
            backtrack(n, m, path)
            path.pop()

n, m = map(int, sys.stdin.readline().split())
backtrack(n, m, [])