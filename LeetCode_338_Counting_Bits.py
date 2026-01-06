from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        dp[0] = 0
        offset = 1
        for i in range(1, n+1):
            if i % offset == 0:
                offset = i
            dp[i] = 1 + dp[i%offset]
        return dp

if __name__ == "__main__":
    n = 0
    solution = Solution()
    result = solution.countBits(n)
    print(result)
