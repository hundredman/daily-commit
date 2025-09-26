# https://www.acmicpc.net/problem/1049
# 기타줄 - Greedy

n, m = map(int, input().split())

for i in range(m):
    if i == 0:
        pack_min, single_min = map(int, input().split())
    else:
        pack, single = map(int, input().split())
        pack_min = min(pack_min, pack)
        single_min = min(single_min, single)

if pack_min < single_min * 6:
    result = (n // 6) * pack_min + min(pack_min, (n % 6) * single_min)
else:
    result = n * single_min

print(result)