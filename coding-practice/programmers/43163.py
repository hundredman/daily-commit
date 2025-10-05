# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 단어 변환 - BFS

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def can_transform(word1, word2):
        diff = sum(c1 != c2 for c1, c2 in zip(word1, word2))
        return diff == 1

    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps
        
        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))
    
    return 0