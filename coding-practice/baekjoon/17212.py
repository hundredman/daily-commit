# https://www.acmicpc.net/problem/17212
# 달나라 토끼를 위한 구매대금 지불 도우미

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