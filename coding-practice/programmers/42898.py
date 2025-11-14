# https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=python3
# 등굣길 - DP

def solution(m, n, puddles):
    MOD = 1_000_000_007
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    puddle_set = set()
    for col, row in puddles:
        puddle_set.add((row, col))
        
    dp[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if (i, j) in puddle_set:
                dp[i][j] = 0
            else:
                from_up = dp[i - 1][j]
                from_left = dp[i][j - 1]
                dp[i][j] = (from_up + from_left) % MOD
                
    return dp[n][m]