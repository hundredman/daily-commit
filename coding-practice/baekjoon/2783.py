# https://www.acmicpc.net/problem/2783
# 삼각 김밥

x, y = map(int, input().split())
min_price = (x / y) * 1000
n = int(input())

for _ in range(n):
    xi, yi = map(int, input().split())
    current_price = (xi / yi) * 1000
    
    if current_price < min_price:
        min_price = current_price

print(f"{min_price:.2f}")