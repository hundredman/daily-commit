# https://www.acmicpc.net/problem/2292
# 벌집

N = int(input())

if N == 1:
    print(1)
else:
    rooms = 1
    count = 1

    while N > rooms:
        rooms += 6 * count
        count += 1
    
    print(count)
