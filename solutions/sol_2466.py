class Solution:
    @staticmethod
    def count_good_strings(low: int, high: int, zero: int, one: int) -> int:
        answer = 0
        mod = 10**9 + 7
        dp = [-1] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            res = 0
            if i - zero >= 0:
                res = (res + dp[i - zero]) % mod
            if i - one >= 0:
                res = (res + dp[i - one]) % mod
            dp[i] = res
            if low <= i <= high:
                answer = (answer + res) % mod
        return answer
