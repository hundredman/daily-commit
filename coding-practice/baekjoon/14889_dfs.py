# https://www.acmicpc.net/problem/14889
# 스타트와 링크 - Depth-First Search

import sys
import itertools

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_diff = float('inf')

def calc_score(group):
    score = 0
    for i, j in itertools.combinations(group, 2):
        score += graph[i][j] + graph[j][i]
    return score

def dfs(depth, team_a):
    global min_diff

    if len(team_a) == n // 2:
        team_b = [i for i in range(n) if i not in team_a]

        score_a = calc_score(team_a)
        score_b = calc_score(team_b)

        diff = abs(score_a - score_b)
        min_diff = min(min_diff, diff)
        return

    for i in range(depth, n):
        if min_diff == 0:
            break
        dfs(i + 1, team_a + [i])

dfs(1, [0])
print(min_diff)