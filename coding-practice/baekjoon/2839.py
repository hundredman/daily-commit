# https://www.acmicpc.net/problem/2839
# 설탕 배달 - Greedy Algorithm

n = int(input())

bag_count = 0

while n >= 0:
    if n % 5 == 0:
        bag_count += (n // 5)
        print(bag_count)
        break
    n -= 3
    bag_count += 1
else:
    print(-1)