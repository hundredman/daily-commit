# https://www.acmicpc.net/problem/4781
# 사탕 가게 - Unbounded Knapsack Problem (Dynamic Programming)

import sys
input = sys.stdin.readline

# 0 0.00이 입력될 때까지 무한 반복
while True:
    line = input().split()
    
    # 입력이 비어있으면 종료 (EOF 대비)
    if not line:
        break
        
    n = int(line[0])
    m_str = line[1]
    
    # 1. 종료 조건 확인
    if n == 0 and m_str == '0.00':
        break
        
    # 2. 돈을 정수로 변환 (소수점 오차 방지)
    # 8.00 -> 800
    # (0.5를 더하는 것은 부동소수점 오차를 방지하는 표준적인 기법)
    M = int(float(m_str) * 100 + 0.5) 

    # 3. DP 테이블 (기록장) 초기화
    # dp[i] = i원으로 살 수 있는 최대 칼로리
    dp = [0] * (M + 1)
    
    # 4. 사탕 정보 입력
    candies = []
    for _ in range(n):
        c_str, p_str = input().split()
        c = int(c_str)
        p = int(float(p_str) * 100 + 0.5)
        candies.append((c, p)) # (칼로리, 가격)

    # 5. DP 점화식 실행 (O(N*M) - 이 부분이 핵심)
    # 각 사탕에 대해서
    for calories, price in candies:
        # 그 사탕의 가격(price)부터 총 예산(M)까지 
        for j in range(price, M + 1):
            # dp[j] = max( (이 사탕을 안 샀을 때의 최대 칼로리), 
            #              ( (j-price)원으로 산 최대 칼로리 + 이 사탕 칼로리 ) )
            dp[j] = max(dp[j], dp[j - price] + calories)

    # 6. 최종 결과 출력
    print(dp[M])