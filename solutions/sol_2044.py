from typing import List


class Solution:
    @staticmethod
    def count_max_or_subsets(nums: List[int]) -> int:
        n = len(nums)
        target = 0
        for num in nums:
            target |= num

        answer = 0

        def dfs(cur, value):
            nonlocal answer

            if cur == n:
                if value == target:
                    answer += 1
                return
            dfs(cur + 1, value)
            dfs(cur + 1, value | nums[cur])

        dfs(0, 0)
        return answer
