from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def num_ways(words: List[str], target: str) -> int:
        m = len(words[0])
        alpha_index = [[] for _ in range(26)]
        alpha_index_count = [[0] * 26 for _ in range(m)]
        mod = 10**9 + 7
        for i in range(m):
            for word in words:
                alpha = ord(word[i]) - ord("a")
                if not alpha_index[alpha] or alpha_index[alpha][-1] != i:
                    alpha_index[alpha].append(i)
                alpha_index_count[i][alpha] += 1

        dp = [[-1] * 1000 for _ in range(len(target))]

        def dfs(cur, start):
            if cur == len(target):
                return 1
            if start == 1000:
                return 0
            if dp[cur][start] == -1:
                alpha = ord(target[cur]) - ord("a")
                cand = alpha_index[alpha]
                s = bisect_left(cand, start)
                res = 0
                if s < len(cand):
                    res = (
                        (dfs(cur, cand[s] + 1))
                        + dfs(cur + 1, cand[s] + 1) * alpha_index_count[cand[s]][alpha]
                    ) % mod
                dp[cur][start] = res
            return dp[cur][start]

        return dfs(0, 0)
