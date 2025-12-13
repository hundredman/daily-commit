# https://school.programmers.co.kr/learn/courses/30/lessons/62048
# 멀쩡한 사각형 - 수학, 최대공약수(GCD)

import math

def solution(w, h):
    # 전체 사각형 개수
    total_squares = w * h
    
    # 대각선이 지나가는(못 쓰는) 사각형 개수
    # 공식: w + h - (w와 h의 최대공약수)
    unusable_squares = w + h - math.gcd(w, h)
    
    # 남은 사각형 개수 반환
    return total_squares - unusable_squares