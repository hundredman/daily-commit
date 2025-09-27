# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버 - Depth-First Search

def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(index, total):
        nonlocal answer
        if index == n:
            if total == target:
                answer += 1
            return
        
        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])

    dfs(0, 0)
    return answer