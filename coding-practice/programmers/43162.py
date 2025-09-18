# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
# 네트워크

def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(start_node):
        visited[start_node] = True
        for i in range(n):
            if computers[start_node][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer