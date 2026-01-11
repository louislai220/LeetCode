from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum %2 != 0:
            return False
        target = sum // 2

        memo = {}
        def dfs(target, index) -> bool:
            if target == 0:
                return True
            if target < 0 or index >= len(nums):
                return False
            if (target, index) in memo:
                return memo[(target, index)]
            result = dfs(target - nums[index], index + 1) or dfs(target, index + 1)
            memo[(target, index)] = result
            return result
        return dfs(target, 0)


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    solution = Solution()
    result = solution.canPartition(nums)
    print(result)