from typing import List


class Solution:
    @staticmethod
    def generate_parenthesis(n: int) -> List[str]:
        answer = []

        def dfs(l, r, st):
            if l == r == 0:
                answer.append("".join(st))
            if l:
                st.append("(")
                dfs(l - 1, r, st)
                st.pop()
            if r and l < r:
                st.append(")")
                dfs(l, r - 1, st)
                st.pop()

        dfs(n, n, [])
        return answer
