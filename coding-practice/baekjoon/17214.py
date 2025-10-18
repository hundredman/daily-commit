# https://www.acmicpc.net/problem/17214
# 다항 함수의 적분

import sys

# 다항식을 한 줄로 입력받습니다.
polynomial = sys.stdin.readline().strip()

a = 0  # x의 계수
b = 0  # 상수항

# 1. 중간에 있는 '+'나 '-' 부호를 찾아 항을 분리합니다.
# 맨 앞의 부호는 첫 항의 것이므로, 두 번째 글자부터 탐색합니다.
split_pos = -1
for i in range(1, len(polynomial)):
    if polynomial[i] == '+' or polynomial[i] == '-':
        split_pos = i
        break

# 2. 찾은 분리 위치에 따라 계수(a)와 상수(b)를 정확히 파싱합니다.
if split_pos != -1:  # 항이 두 개인 경우 (e.g., "6x+6", "-2x-4")
    x_term_str = polynomial[:split_pos]
    const_term_str = polynomial[split_pos:]
    a = int(x_term_str.replace('x', '')) # 'x'를 지우고 숫자로 변환
    b = int(const_term_str)
else:  # 항이 하나만 있는 경우 (e.g., "6x", "-10")
    if 'x' in polynomial:
        # x항만 있는 경우
        a = int(polynomial.replace('x', ''))
    else:
        # 상수항만 있는 경우
        b = int(polynomial)

# 3. 적분 규칙을 적용합니다.
# f(x) = ax + b  ->  ∫f(x)dx = (a/2)x² + bx + W
integrated_a = a // 2
integrated_b = b

# 4. 출력 형식에 맞게 문자열 조각들을 만듭니다.
result_parts = []

# xx항 추가
if integrated_a != 0:
    if integrated_a == 1:
        result_parts.append("xx")
    elif integrated_a == -1:
        result_parts.append("-xx")
    else:
        result_parts.append(f"{integrated_a}xx")

# x항 추가 (★★★ 오류를 수정한 부분 ★★★)
if integrated_b != 0:
    sign = ""
    # 이미 앞에 항이 있고, 현재 항이 양수일 때만 '+'를 붙입니다.
    if len(result_parts) > 0 and integrated_b > 0:
        sign = "+"
    
    # 계수가 1 또는 -1일 때 숫자 '1'을 생략하는 로직 추가
    if integrated_b == 1:
        result_parts.append(f"{sign}x")
    elif integrated_b == -1:
        result_parts.append("-x")
    else:
        result_parts.append(f"{sign}{integrated_b}x")

# 5. 최종 결과물을 출력합니다.
if not result_parts:  # 입력이 "0" 이라서 적분 결과 항이 없는 경우
    print("W")
else:
    # 모든 조각을 합치고 마지막에 "+W"를 붙입니다.
    print("".join(result_parts) + "+W")