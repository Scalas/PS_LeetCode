class Solution:
    @staticmethod
    def repeated_substring_pattern(s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i:
                continue
            word = s[:i]
            res = True
            for j in range(i, n, i):
                if s[j : j + i] != word:
                    res = False
                    break
            if res:
                return True
        return False
