class Solution:
    @staticmethod
    def find_the_longest_substring(s: str) -> int:
        n = len(s)
        d = dict()
        mask = 0
        bit = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        answer = 0
        for i in range(n):
            if s[i] in bit:
                b = bit[s[i]]
                mask = (~mask & b) | (mask & ~b)
                if mask not in d:
                    d[mask] = i
            if mask == 0:
                answer = i + 1
            else:
                answer = max(answer, i - d[mask])

        return answer
