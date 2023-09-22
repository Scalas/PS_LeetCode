class Solution:
    @staticmethod
    def is_subsequence(s: str, t: str) -> bool:
        n = len(t)
        idx = 0
        for cur in s:
            while idx < n and t[idx] != cur:
                idx += 1
            if idx == n:
                return False
            idx += 1
        return True
