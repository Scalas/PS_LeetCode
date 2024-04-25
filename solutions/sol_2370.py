class Solution:
    @staticmethod
    def longest_ideal_string(s: str, k: int) -> int:
        order = list(map(lambda x: ord(x) - ord("a"), s))
        dp = [0] * 26
        dp[order[-1]] = 1
        for i in range(len(s) - 2, -1, -1):
            o = order[i]
            res = 1
            for nxt in range(max(o - k, 0), min(o + k + 1, 26)):
                res = max(res, dp[nxt] + 1)
            dp[o] = max(dp[o], res)
        return max(dp)
