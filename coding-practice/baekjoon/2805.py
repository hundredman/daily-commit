# https://www.acmicpc.net/problem/2805
# 나무 자르기 - Binary Search

import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

result = 0
while start <= end:
    mid = (start + end) // 2
    
    total_cut = sum(t - mid for t in trees if t > mid)

    if total_cut >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)