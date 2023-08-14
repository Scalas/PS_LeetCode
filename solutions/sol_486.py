from typing import List


class Solution:
    @staticmethod
    def predict_the_winner(nums: List[int]) -> bool:
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]

        def dfs(s, e, turn):
            if s > e:
                return 0
            if dp[s][e] == -1:
                if turn:
                    dp[s][e] = min(dfs(s, e - 1, 1 - turn), dfs(s + 1, e, 1 - turn))
                else:
                    dp[s][e] = max(
                        dfs(s, e - 1, 1 - turn) + nums[e],
                        dfs(s + 1, e, 1 - turn) + nums[s],
                    )
            return dp[s][e]

        return dfs(0, n - 1, 0) * 2 - sum(nums) >= 0
