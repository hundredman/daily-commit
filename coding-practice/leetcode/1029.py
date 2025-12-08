# https://leetcode.com/problems/two-city-scheduling/
# Two City Scheduling - Greedy

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 1. (aCost - bCost)를 기준으로 오름차순 정렬
        # x[0]은 A비용, x[1]은 B비용
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2  # 전체 인원의 절반
        
        # 2. 앞의 n명은 A도시로 가는 비용 더하기
        for i in range(n):
            total_cost += costs[i][0]
            
        # 3. 뒤의 n명은 B도시로 가는 비용 더하기
        for i in range(n, 2 * n):
            total_cost += costs[i][1]
            
        return total_cost