class Solution:
    @staticmethod
    def find_the_difference(s: str, t: str) -> str:
        count_1 = [0] * 26
        count_2 = [0] * 26
        for c in s:
            count_1[ord(c) - ord("a")] += 1
        for c in t:
            count_2[ord(c) - ord("a")] += 1
        for i in range(26):
            if count_2[i] - count_1[i] == 1:
                return chr(i + ord("a"))
