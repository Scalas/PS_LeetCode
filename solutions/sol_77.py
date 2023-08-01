from typing import List


class Solution:
    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(cur, st):
            if cur == k:
                answer.append(st[:])
                return
            last = 0 if not st else st[-1]
            for select in range(last + 1, n - k + cur + 2):
                st.append(select)
                dfs(cur + 1, st)
                st.pop()

        dfs(0, [])
        return answer
