class Solution:
    @staticmethod
    def number_of_arrays(s: str, k: int) -> int:
        n = len(s)
        mod = 10**9 + 7

        # dp[i] 는 s[i] 부터 1 이상 k 이하의 수로만 이루어진 배열로 분할하는 경우의 수
        dp = [-1] * n

        def dfs(cur):
            if cur == n:
                return 1

            if dp[cur] == -1:
                res = 0
                num = 0

                for nxt in range(cur, n):
                    num = num * 10 + int(s[nxt])

                    # num이 이미 k를 넘어섰다면 더 이상 탐색할 필요가 없음
                    if num > k:
                        break

                    # 수를 여기서 자를 경우 다음 수가 0으로 시작해야한다면 자를 수 없음
                    if nxt + 1 < n and s[nxt + 1] == "0":
                        continue

                    res = (res + dfs(nxt + 1)) % mod
                dp[cur] = res

            return dp[cur]

        return dfs(0)
