# https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    
    # left부터 right까지 모든 수를 확인
    for i in range(left, right + 1):
        
        # 제곱근이 정수이면 제곱수입니다.
        # 예: 16의 0.5승(루트)은 4.0 -> 정수이므로 제곱수 O
        # 예: 15의 0.5승(루트)은 3.87... -> 정수가 아니므로 제곱수 X
        if int(i ** 0.5) == i ** 0.5:
            answer -= i  # 약수가 홀수개이므로 뺌
        else:
            answer += i  # 약수가 짝수개이므로 더함
            
    return answer