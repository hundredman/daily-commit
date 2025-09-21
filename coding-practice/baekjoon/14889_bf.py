# https://www.acmicpc.net/problem/14889
# 스타트와 링크 - Brute Force

import sys
import itertools

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
player = list(range(n))

min_diff = float('inf')

def calc_score(group):
    score = 0
    for i, j in itertools.combinations(group, 2):
        score += graph[i][j] + graph[j][i]
    return score

for team in itertools.combinations(player, n//2):
    if 0 not in team:
        continue

    start = set(team)
    link = set(player) - start
    
    score_start = calc_score(start)
    score_link = calc_score(link)

    diff = abs(score_start - score_link)
    min_diff = min(min_diff, diff)

print(min_diff)