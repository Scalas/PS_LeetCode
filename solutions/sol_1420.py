class Solution:
    @staticmethod
    def num_of_arrays(n: int, m: int, k: int) -> int:
        if m < k:
            return 0

        dp = [[[-1] * 51 for _ in range(101)] for _ in range(51)]
        mod = 10**9 + 7

        sq = [[(i**j) % mod for j in range(51)] for i in range(101)]

        def dfs(cur, last, remain):
            if cur == n:
                return 1
            if dp[cur][last][remain] == -1:
                res = 0
                # select current number that is not new max
                if n - cur > remain:
                    for i in range(1, last + 1):
                        res = (res + dfs(cur + 1, last, remain)) % mod
                # select current number that is new max
                if remain:
                    for i in range(last + 1, m - remain + 2):
                        res = (res + dfs(cur + 1, i, remain - 1)) % mod
                dp[cur][last][remain] = res
            return dp[cur][last][remain]

        return dfs(0, 0, k)
