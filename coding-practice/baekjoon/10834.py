# https://www.acmicpc.net/problem/10834
# 벨트

n = int(input())

rotation = 1
direction = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    
    rotation = rotation * b / a
    
    if c == 1:
        direction = 1 - direction

print(direction, int(rotation))