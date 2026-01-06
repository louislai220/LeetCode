class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[i]
if __name__ == "__main__":
    n = 25
    solution = Solution()
    result= solution.tribonacci(n)
    print(result)