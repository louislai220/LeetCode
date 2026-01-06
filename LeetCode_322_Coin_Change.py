from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount:int) -> int:
        cache = {0:0}
        def min_coin(amt: int) -> int:
            if amt in cache:
                return cache[amt]    
            minn = float("inf")
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    continue
                minn = min(minn, 1 + min_coin(diff))
            cache[amt] = minn
            return minn
        min_coin(amount)
        if cache[amount] == float('inf'):
            return -1
        return cache[amount]

    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        for i in range(1, amount+1):
            minn = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    continue
                minn = min(minn, 1 + dp[i - coin])
            dp[i] = minn
        return dp[amount]

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    solution = Solution()
    result = solution.coinChange2(coins, amount)
    print(result)