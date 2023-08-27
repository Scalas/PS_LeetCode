from typing import List


class Solution:
    @staticmethod
    def can_cross(stones: List[int]) -> bool:
        n = len(stones)
        stone_idx = dict()
        for i in range(n):
            stone_idx[stones[i]] = i

        dp = [[None] * (n + 1) for _ in range(n)]

        def dfs(cur, last):
            if cur == n - 1:
                return True
            if dp[cur][last] is None:
                res = False
                for jump in range(last - 1, last + 2):
                    if jump <= 0:
                        continue
                    nxt = stone_idx.get(stones[cur] + jump, -1)
                    if nxt == -1:
                        continue
                    if dfs(nxt, jump):
                        res = True
                        break
                dp[cur][last] = res
            return dp[cur][last]

        return dfs(0, 0)
