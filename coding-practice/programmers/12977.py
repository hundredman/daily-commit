# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기 - Brute Force, Combinations

from itertools import combinations

# 소수 판별 함수
def is_prime(num):
    if num < 2: 
        return False
    # 2부터 num의 제곱근까지만 나누어 떨어지는지 확인하면 됨
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    # nums 리스트에서 3개의 숫자를 뽑는 모든 조합을 구함
    for comb in combinations(nums, 3):
        total = sum(comb)  # 3개 숫자의 합
        if is_prime(total): # 합이 소수인지 확인
            answer += 1
            
    return answer