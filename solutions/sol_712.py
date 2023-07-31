class Solution:
    @staticmethod
    def minimum_delete_sum(s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        s1 = list(map(lambda x: ord(x), s1))
        s2 = list(map(lambda x: ord(x), s2))
        total = sum(s1) + sum(s2)
        dp = [[total] * (m + 1) for _ in range(n + 1)]
        answer = total
        for i in range(n):
            for j in range(m):
                reduce = 0
                if s1[i] == s2[j]:
                    reduce -= s1[i] * 2
                res = min(dp[i - 1][j - 1] + reduce, dp[i - 1][j], dp[i][j - 1])
                answer = min(answer, res)
                dp[i][j] = res
        return answer
