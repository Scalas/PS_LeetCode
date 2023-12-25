class Solution:
    @staticmethod
    def num_decoding(s: str) -> int:
        n = len(s)
        dp = [0] * n
        if s[0] != "0":
            dp[0] = 1

        for i in range(1, n):
            c = int(s[i])
            dp[i] = 0 if s[i] == "0" else dp[i - 1]
            pre = int(s[i - 1])
            if pre == 1 or (pre == 2 and c <= 6):
                dp[i] += 1 if i < 2 else dp[i - 2]
        return dp[-1]
