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

    team_a = set(team)
    team_b = set(player) - team_a
    
    score_a = calc_score(team_a)
    score_b = calc_score(team_b)

    diff = abs(score_a - score_b)
    min_diff = min(min_diff, diff)

    if min_diff == 0:
        break

print(min_diff)