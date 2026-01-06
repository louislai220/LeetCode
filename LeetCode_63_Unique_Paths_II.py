from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstaclesGrid: List[List[int]]) -> int:
        col = len(obstaclesGrid[0])
        row = len(obstaclesGrid)

        if obstaclesGrid[0][0] == 1:
            return 0
        dp = [ [0] * (col + 1) for _ in range(row + 1)]
        dp[1][1] = 1

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if i == 1 and j == 1 or obstaclesGrid[i-1][j-1] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[row][col]
if __name__ == "__main__":
    obstaclesGrid=[[1]]
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstaclesGrid)
    print(result)
