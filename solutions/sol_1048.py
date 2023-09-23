from typing import List


class Solution:
    @staticmethod
    def longest_str_chain(words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        n = len(words)

        def check(s1, s2):
            l1, l2 = len(s1), len(s2)
            if l1 - l2 != 1:
                return False
            idx = 0
            for c in s2:
                while idx < l1 and s1[idx] != c:
                    idx += 1
                if idx == l1:
                    return False
                idx += 1
            return True

        dp = [[-1] * n for _ in range(n)]

        def dfs(cur, pre):
            if cur == n:
                return 0
            if dp[cur][pre] == -1:
                res = dfs(cur + 1, pre)
                if pre == -1 or check(words[cur], words[pre]):
                    res = max(res, dfs(cur + 1, cur) + 1)
                dp[cur][pre] = res
            return dp[cur][pre]

        return dfs(0, -1)
