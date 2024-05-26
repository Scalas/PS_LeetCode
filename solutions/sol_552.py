from sys import setrecursionlimit

setrecursionlimit(200000)


class Solution:
    @staticmethod
    def check_record(n: int) -> int:
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        mod = 10**9 + 7

        def dfs(cur, ac, lc):
            nonlocal mod
            if cur == n:
                return 1
            if dp[cur][ac][lc] == -1:
                res = 0
                res += dfs(cur + 1, ac, 0)
                if ac < 1:
                    res = (res + dfs(cur + 1, ac + 1, 0)) % mod
                if lc < 2:
                    res = (res + dfs(cur + 1, ac, lc + 1)) % mod
                dp[cur][ac][lc] = res
            return dp[cur][ac][lc]

        return dfs(0, 0, 0)
