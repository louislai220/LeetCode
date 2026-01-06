from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [0] * numRows
        result=[]
        for i in range(0, numRows):
            row = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(dp[j-1] + dp[j])
            dp = row
            result.append(row)
        return result

if __name__ == "__main__":
    n = 5
    solution = Solution()
    result = solution.generate(n)
    print(result)