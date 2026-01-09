from typing import List
class Solution():
    def change(self, amount:int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins)+1)]
        for i in range(1,len(dp)):
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i -1]]
        return dp[len(coins)][amount]    

        

if __name__ == "__main__":
    amount = 3
    coins=[1,2]
    solution = Solution()
    result = solution.change(amount, coins)
    print(result)