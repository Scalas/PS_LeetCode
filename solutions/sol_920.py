class Solution:
    @staticmethod
    def num_music_playlists(n: int, goal: int, k: int) -> int:
        m = goal
        mod = 10**9 + 7

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i, m + 1):
                dp[i][j] = (
                    dp[i - 1][j - 1] * (n - i + 1) + dp[i][j - 1] * (i - min(j - 1, k))
                ) % mod
        return dp[n][m]
