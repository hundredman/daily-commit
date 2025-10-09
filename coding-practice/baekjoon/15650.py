# https://www.acmicpc.net/problem/15650
# N과 M (2) - Combinations

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

nums = list(range(1, n + 1))

for combo in combinations(nums, m):
    print(*combo)