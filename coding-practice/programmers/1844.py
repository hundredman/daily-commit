# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 게임 맵 최단거리 - BFS

from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False]*cols for _ in range(rows)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
               
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (rows-1, cols-1):
            return dist
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))
    return -1