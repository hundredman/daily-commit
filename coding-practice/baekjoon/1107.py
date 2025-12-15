# https://www.acmicpc.net/problem/1107
# 리모컨 - Brute Force

import sys
input = sys.stdin.readline

def solve():
    # 목표 채널 N
    N = int(input())
    # 고장난 버튼 개수 M
    M = int(input())
    
    # 고장난 버튼 집합 (검색 속도를 위해 set 사용)
    broken = set()
    if M > 0:
        broken = set(input().split())
    
    # 1. 단순히 +,- 만 눌러서 이동하는 경우 (초기 최솟값)
    min_press = abs(N - 100)
    
    # 2. 0번부터 1,000,000번 채널까지 모두 확인 (Brute Force)
    # N이 500,000이므로 위에서 내려오는 경우를 고려해 약 2배 범위까지 탐색
    for num in range(1000001):
        num_str = str(num)
        
        # 현재 채널 번호(num)를 누를 수 있는지 확인
        is_possible = True
        for digit in num_str:
            if digit in broken: # 고장난 버튼이 포함되어 있으면 불가능
                is_possible = False
                break
        
        # 고장난 버튼 없이 누를 수 있는 채널이라면
        if is_possible:
            # 버튼 누른 횟수 = (채널 번호 누르는 횟수) + (+/- 누르는 횟수)
            # len(num_str): 숫자 버튼 누른 횟수
            # abs(num - N): +,- 버튼 누른 횟수
            current_press = len(num_str) + abs(num - N)
            
            # 최솟값 갱신
            if current_press < min_press:
                min_press = current_press
                
    print(min_press)

solve()