from typing import List


class Solution:
    @staticmethod
    def min_extra_char(s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [-1] * len(s)

        def dfs(cur):
            if cur == n:
                return 0
            if dp[cur] == -1:
                l = n - cur
                res = l
                for word in dictionary:
                    if len(word) > l:
                        continue
                    match = True
                    for i in range(len(word)):
                        if s[cur + i] != word[i]:
                            match = False
                            break
                    if match:
                        res = min(res, dfs(cur + len(word)))
                res = min(res, dfs(cur + 1) + 1)
                dp[cur] = res
            return dp[cur]

        return dfs(0)
