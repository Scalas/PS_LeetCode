from typing import List


class Solution:
    @staticmethod
    def max_value_of_coins(piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1] * (k + 1) for _ in range(n)]

        def dfs(pile_id, remain):
            if pile_id == n:
                return 0

            if dp[pile_id][remain] == -1:
                picked = 0
                count = 0
                res = dfs(pile_id + 1, remain)
                for num in piles[pile_id]:
                    if not remain - count:
                        break
                    count += 1
                    picked += num
                    res = max(res, picked + dfs(pile_id + 1, remain - count))
                dp[pile_id][remain] = res
            return dp[pile_id][remain]

        return dfs(0, k)
