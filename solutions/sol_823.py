from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def num_factored_binary_trees(arr: List[int]) -> int:
        div = defaultdict(set)
        for num1 in arr:
            for num2 in arr:
                m = num1 * num2
                div[m].add((num1, num2))

        dp = dict()
        mod = 10**9 + 7

        def dfs(num):
            if num not in dp:
                res = 1
                for u, v in div[num]:
                    res = (res + dfs(u) * dfs(v)) % mod
                dp[num] = res
            return dp[num]

        return sum(map(lambda x: dfs(x), arr)) % mod
