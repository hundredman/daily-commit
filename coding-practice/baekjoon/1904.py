# https://www.acmicpc.net/problem/1904
# 01타일 - DP

import sys

N = int(sys.stdin.readline())

MOD = 15746

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    a = 1
    b = 2

    for i in range(3, N + 1):
        current = (a + b) % MOD
        a = b
        b = current

    print(b)