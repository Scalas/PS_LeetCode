from typing import List


class Solution:
    @staticmethod
    def longest_subsequence(arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        for i in range(n - 1, -1, -1):
            cur = arr[i]
            nxt = cur + difference
            if nxt in dp:
                dp[cur] = max(dp.get(cur, 0), dp[nxt] + 1)
            else:
                dp[cur] = max(dp.get(cur, 0), 1)
        return max(dp.values())
