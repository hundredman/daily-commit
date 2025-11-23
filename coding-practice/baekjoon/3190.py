# https://www.acmicpc.net/problem/3190
# 뱀

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1  # 사과 위치 표시

L = int(input())
moves = {}
for _ in range(L):
    t, d = input().split()
    moves[int(t)] = d

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 1, 1
direction = 0

snake = deque([(1, 1)])
board[1][1] = 2  # 뱀 위치 표시

time = 0
while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 1 or nx > N or ny < 1 or ny > N:
        break
    if board[nx][ny] == 2:
        break

    if board[nx][ny] == 1:
        board[nx][ny] = 2
        snake.append((nx, ny))
    else:
        board[nx][ny] = 2
        snake.append((nx, ny))
        tx, ty = snake.popleft()
        board[tx][ty] = 0

    x, y  = nx, ny

    if time in moves:
        if moves[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(time)