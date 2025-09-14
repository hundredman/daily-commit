# https://www.acmicpc.net/problem/10834
# 벨트간 회전수 비를 이용해 최종 바퀴의 회전수를 구하는 문제

n = int(input())

rotation = 1
direction = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    
    rotation = rotation * b / a
    
    if c == 1:
        direction = 1 - direction

print(direction, int(rotation))