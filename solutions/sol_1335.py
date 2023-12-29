from typing import List


class Solution:
    @staticmethod
    def min_difficulty(job_difficulty: List[int], d: int) -> int:
        n = len(job_difficulty)

        if n < d:
            return -1

        dp = [[-1] * n for _ in range(d)]

        def dfs(cur, idx):
            if cur == d - 1:
                return max(job_difficulty[idx:])
            if dp[cur][idx] == -1:
                res = 10**9
                max_difficulty = 0
                for end in range(idx, n - d + cur + 1):
                    max_difficulty = max(max_difficulty, job_difficulty[end])
                    res = min(res, max_difficulty + dfs(cur + 1, end + 1))
                dp[cur][idx] = res
            return dp[cur][idx]

        return dfs(0, 0)
