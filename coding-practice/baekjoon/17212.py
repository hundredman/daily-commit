# https://www.acmicpc.net/problem/17212
# 1, 2, 5, 7원짜리 동전을 이용해 n원을 만드는 최소 동전 갯수를 구하는 문제

def remainder(n):
    coins = [1, 2, 5, 7]
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = float('inf')
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[n]

n = int(input())
print(remainder(n))