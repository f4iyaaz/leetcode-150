class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        total_cost = 0
        memo = {0:0, 1:0}
        def minCost(length):
            if length in memo:
                return memo[length]
            memo[length] = min(minCost(length - 1) + cost[length - 1], minCost(length - 2) + cost[length - 2])
            return memo[length]
        return minCost(length)

  # Runtime: O(n)
