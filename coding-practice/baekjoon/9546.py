# https://www.acmicpc.net/problem/9546
# 3000번 버스

def passengers(k):
    for i in range(k):
        if i == 0:
            n = 1
        else:
            n = n * 2 + 1
    return n

t = int(input())
for _ in range(t):
    k = int(input())
    print(passengers(k))