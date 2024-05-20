from typing import List


class Solution:
    @staticmethod
    def subset_xor_sum(nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        def xor(x, y):
            return (~x & y) | (x & ~y)

        def dfs(cur, res):
            nonlocal answer
            if cur == n:
                if res != -1:
                    answer += res
                return
            dfs(cur + 1, xor(res, nums[cur]) if res != -1 else nums[cur])
            dfs(cur + 1, res)

        dfs(0, -1)

        return answer
