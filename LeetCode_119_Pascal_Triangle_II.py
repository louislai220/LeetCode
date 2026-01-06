from typing import List
class Solution:
    def getRow(self, rowIndex: int) ->List[int]:
        n = rowIndex + 1
        dp = 0 * [n]

        for i in range(0, n):
            result=[]
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    result.append(1)
                else:
                    result.append(dp[j-1] + dp[j])
            dp = result
        return result


if __name__ == "__main__":
    rowIndex = 0
    solution = Solution()
    result = solution.getRow(rowIndex)
    print(result)