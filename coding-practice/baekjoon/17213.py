# https://www.acmicpc.net/problem/17213
# 생일 파티

import math

n = int(input())
m = int(input())

result = math.comb(m - 1, n - 1)

print(result)