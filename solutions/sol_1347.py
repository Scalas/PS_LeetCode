class Solution:
    @staticmethod
    def min_steps(s: str, t: str) -> int:
        scount = [0] * 26
        tcount = [0] * 26
        for c in s:
            scount[ord(c) - ord("a")] += 1
        for c in t:
            tcount[ord(c) - ord("a")] += 1
        return sum([abs(scount[i] - tcount[i]) for i in range(26)]) // 2
