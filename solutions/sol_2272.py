from collections import Counter


class Solution:
    @staticmethod
    def largest_variance(s: str) -> int:
        INF = 10**9
        n = len(s)
        s = list(map(lambda x: ord(x) - ord("a"), list(s)))
        alpha_count = Counter(s)
        answer = 0
        for i in range(26):
            for j in range(26):
                if i == j:
                    continue
                ic, jc = alpha_count.get(i, 0), alpha_count.get(j, 0)
                if not ic or not jc:
                    continue
                if ic == jc == 1:
                    continue
                dp = [-INF] * 4
                if s[n - 1] == i:
                    dp[1] = 1
                elif s[n - 1] == j:
                    dp[2] = -1
                for cur in range(n - 2, -1, -1):
                    state = 1 if s[cur] == i else 2 if s[cur] == j else 0
                    cdp = [-INF] * 4
                    if state == 0:
                        continue
                    elif state == 1:
                        cdp[1] = 1
                        if dp[1] > 0:
                            cdp[1] += dp[1]
                        if dp[3] != -INF:
                            cdp[3] = dp[3] + 1
                        if dp[2] != -INF:
                            cdp[3] = max(cdp[3], 0)
                    else:
                        cdp[2] = -1
                        if dp[1] != -INF:
                            cdp[3] = dp[1] - 1
                        if dp[3] != -INF:
                            cdp[3] = max(cdp[3], dp[3] - 1)
                    dp = cdp
                    answer = max(answer, dp[3])
        return answer
