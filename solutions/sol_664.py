from collections import defaultdict


class Solution:
    @staticmethod
    def strange_printer(s: str) -> int:
        st = []
        for c in s:
            if st and st[-1] == c:
                continue
            st.append(c)
        s = "".join(st)
        n = len(s)
        idx = defaultdict(list)
        for i in range(n):
            idx[s[i]].append(i)
        dp = [[[-1] * 27 for _ in range(n)] for _ in range(n)]

        def dfs(l, r, bg):
            if l > r:
                return 0
            ch = ord(s[l]) - ord("a") + 1
            if l == r:
                return 1 if ch != bg else 0
            if dp[l][r][bg] == -1:
                res = 101
                if s[l] == s[r]:
                    res = dfs(l + 1, r - 1, ch) + (1 if ch != bg else 0)
                else:
                    for mid in idx[s[l]]:
                        if mid >= r:
                            break
                        if mid < l:
                            continue
                        res = min(res, dfs(l, mid, bg) + dfs(mid + 1, r, bg))
                dp[l][r][bg] = res
            return dp[l][r][bg]

        return dfs(0, n - 1, 0)
