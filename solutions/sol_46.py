from typing import List


class Solution:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        visited = [False] * n

        def dfs(cur, st):
            if cur == n:
                answer.append(st[:])
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                st.append(nums[i])
                dfs(cur + 1, st)
                st.pop()
                visited[i] = False

        dfs(0, [])
        return answer
