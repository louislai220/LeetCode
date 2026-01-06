from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)
        dp = [0] * (top + 1)

        dp[0], dp[1] = 0, 0
        for i in range(2, top + 1):
            option1 = dp[i-1] + cost[i-1]
            option2 = dp[i-2] + cost[i-2]
            dp[i] = min(option1, option2)
        return dp[top]

if __name__ == "__main__":
    cost = [10,20,50]
    solution = Solution()
    result = solution.minCostClimbingStairs(cost)
    print(result)
