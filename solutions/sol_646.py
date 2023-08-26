from typing import List


class Solution:
    @staticmethod
    def find_longest_chain(pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        pairs = list(map(lambda x: [x[0] + 1000, x[1] + 1000], pairs))

        dp = [[-1] * n for _ in range(n)]

        def dfs(cur, last):
            if cur == n:
                return 0
            if dp[cur][last] == -1:
                start = 0 if last == -1 else pairs[last][1] + 1
                l, r = pairs[cur]
                res = dfs(cur + 1, last)
                if l >= start:
                    res = max(res, dfs(cur + 1, cur) + 1)
                dp[cur][last] = res
            return dp[cur][last]

        return dfs(0, -1)
