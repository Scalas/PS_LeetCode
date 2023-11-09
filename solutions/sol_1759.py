class Solution:
    @staticmethod
    def count_homogenous(s: str) -> int:
        answer = 0
        mod = 10**9 + 7
        pre = s[0]
        cnt = 1
        for c in s[1:]:
            if c == pre:
                cnt += 1
            else:
                answer = (answer + cnt * (cnt + 1) // 2) % mod
                pre = c
                cnt = 1
        return (answer + cnt * (cnt + 1) // 2) % mod
