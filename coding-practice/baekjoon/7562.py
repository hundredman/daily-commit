# https://www.acmicpc.net/problem/7562
# 나이트의 이동 - BFS

import sys
from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(l, start_x, start_y, target_x, target_y):
    if start_x == target_x and start_y == target_y:
        return 0

    visited = [[0] * l for _ in range(l)]
    queue = deque([(start_x, start_y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if nx == target_x and ny == target_y:
                    return visited[nx][ny]

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    l = int(sys.stdin.readline())
    current_x, current_y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())    
    result = bfs(l, current_x, current_y, target_x, target_y)
    print(result)