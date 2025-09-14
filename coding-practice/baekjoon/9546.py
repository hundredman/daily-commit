# https://www.acmicpc.net/problem/9546
# 주어진 규칙에 맞게 정류장의 갯수에 따른 승객의 수를 구하는 문제

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