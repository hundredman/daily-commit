# https://www.acmicpc.net/problem/3040
# 백설 공주와 일곱 난쟁이 - Combination

import sys
from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(sys.stdin.readline()))

for seven_dwarfs in combinations(dwarfs, 7):
    if sum(seven_dwarfs) == 100:
        for dwarf in seven_dwarfs:
            print(dwarf)
        break