# https://www.acmicpc.net/problem/2799
# 블라인드

import sys

# 입력 속도를 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    # M: 층 수, N: 한 층의 창문 개수
    M, N = map(int, input().split())
    
    # 아파트 전체 그리드 입력 받기
    grid = [input().strip() for _ in range(5 * M + 1)]
    
    # 결과 저장용 리스트 (블라인드 0칸~4칸인 창문의 개수)
    result = [0] * 5
    
    # 모든 창문을 순회
    for i in range(M):        # i: 층 인덱스
        for j in range(N):    # j: 창문 인덱스
            
            # 현재 보고 있는 창문의 '내용물' 시작 좌표 (왼쪽 위)
            # 프레임(#)이 1칸, 창문 내용이 4칸이므로 5칸씩 건너뜀 + 1(첫 프레임)
            row = 5 * i + 1
            col = 5 * j + 1
            
            blind_count = 0
            
            # 해당 창문의 4개 행을 확인
            # k는 0, 1, 2, 3 (위에서부터 아래로 4줄)
            for k in range(4):
                if grid[row + k][col] == '*':
                    blind_count += 1
            
            # 해당 블라인드 타입의 개수 증가
            result[blind_count] += 1
            
    # 결과 출력 (공백으로 구분)
    print(*result)

# 실행
solve()