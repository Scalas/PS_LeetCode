from typing import List


class Solution:
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []

        def dfs(cur, s):
            nonlocal n, answer
            if cur == n:
                answer.append(s[:])
                return
            s.append(nums[cur])
            dfs(cur + 1, s)
            s.pop()
            dfs(cur + 1, s)

        dfs(0, [])
        return answer
