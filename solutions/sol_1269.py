class Solution:
    @staticmethod
    def num_ways(steps: int, arr_len: int) -> int:
        mod = 10**9 + 7
        dp = [[-1] * (steps + 1) for _ in range(501)]

        def dfs(cur, step):
            remain = steps - step
            if cur > remain:
                return 0
            if cur == remain:
                return 1

            if dp[cur][step] == -1:
                res = dfs(cur, step + 1)
                if cur > 0:
                    res = (res + dfs(cur - 1, step + 1)) % mod
                if cur < arr_len - 1:
                    res = (res + dfs(cur + 1, step + 1)) % mod
                dp[cur][step] = res
            return dp[cur][step]

        return dfs(0, 0)
