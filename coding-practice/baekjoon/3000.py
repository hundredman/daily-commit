# https://www.acmicpc.net/problem/3000
# 직각 삼각형 - Hash Map

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

x_counts = defaultdict(int)
y_counts = defaultdict(int)

points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    x_counts[x] += 1
    y_counts[y] += 1

total_triangles = 0

for x, y in points:
    count_same_x = x_counts[x] - 1
    count_same_y = y_counts[y] - 1
    total_triangles += (count_same_x * count_same_y)

print(total_triangles)