from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def longest_arith_seq_length(nums: List[int]) -> int:
        n, m = len(nums), 1000
        adj = dict()
        count = Counter(nums)
        dp = [[-1] * (m + 1) for _ in range(n)]
        for i in range(m + 1):
            dp[n - 1][i] = 1
        adj[nums[n - 1]] = n - 1
        for i in range(n - 2, -1, -1):
            num = nums[i]
            for diff in range(m + 1):
                d = diff - 500
                adj_nxt = adj.get(num + d, -1)
                if adj_nxt == -1:
                    dp[i][diff] = 1
                else:
                    dp[i][diff] = dp[adj_nxt][diff] + 1
                adj[num] = i
        return max(max([max(line) for line in dp]), max(count.values()))
