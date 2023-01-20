from typing import List


class Solution:
    @staticmethod
    def find_subsequences(nums: List[int]) -> List[List[int]]:
        sub_array = []
        n = len(nums)
        answer = set()

        def dfs(cur):
            if cur == n:
                if len(sub_array) > 1:
                    answer.add(tuple(sub_array[:]))
                return
            if not sub_array or nums[cur] >= sub_array[-1]:
                sub_array.append(nums[cur])
                dfs(cur + 1)
                sub_array.pop()
            dfs(cur + 1)

        dfs(0)
        return list(answer)

