# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# Average of Levels in Binary Tree - BFS

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        result = []
        
        if not root:
            return result
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            average = level_sum / level_size
            result.append(average)
            
        return result