# https://school.programmers.co.kr/learn/courses/30/lessons/49993?language=python3
# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        filtered_tree = ""
        for s in tree:
            if s in skill:
                filtered_tree += s
        if skill.startswith(filtered_tree):
            answer += 1
    return answer