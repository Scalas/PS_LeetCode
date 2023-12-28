class Solution:
    @staticmethod
    def get_length_of_optimal_compression(s: str, k: int) -> int:
        n = len(s)
        inc_set = {2, 10, 100}
        dp = [[dict() for _ in range(k + 1)] for _ in range(n)]

        def comp(cur, remain, last):
            if cur == n:
                return 0
            if dp[cur][remain].get(last, -1) == -1:
                c = s[cur]
                lc, lcnt = last.split(",")
                lcnt = int(lcnt)
                inc = n - cur
                if lc == c:
                    nlast = f"{lc},{lcnt + 1}"
                    inc = min(
                        inc,
                        (1 if lcnt + 1 in inc_set else 0)
                        + comp(cur + 1, remain, nlast),
                    )
                else:
                    nlast = f"{c},{1}"
                    inc = min(inc, 1 + comp(cur + 1, remain, nlast))
                if remain:
                    inc = min(inc, comp(cur + 1, remain - 1, last))
                dp[cur][remain][last] = inc
            return dp[cur][remain][last]

        return comp(0, k, "-,0")
