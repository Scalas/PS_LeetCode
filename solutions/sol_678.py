class Solution:
    @staticmethod
    def check_valid_string(s: str) -> bool:
        n = len(s)

        def dfs(cur, p):
            if cur == n:
                return p == 0
            if dp[cur][p] is None:
                c = s[cur]
                if c == "(":
                    dp[cur][p] = dfs(cur + 1, p + 1)
                elif c == ")":
                    if not p:
                        return False
                    dp[cur][p] = dfs(cur + 1, p - 1)
                else:
                    dp[cur][p] = (
                        dfs(cur + 1, p)
                        or dfs(cur + 1, p + 1)
                        or (p > 0 and dfs(cur + 1, p - 1))
                    )
            return dp[cur][p]

        dp = [[None] * (n + 1) for _ in range(n)]

        return dfs(0, 0)
