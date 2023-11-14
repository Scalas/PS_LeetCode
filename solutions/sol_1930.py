from bisect import bisect_left, bisect_right


class Solution:
    @staticmethod
    def count_palindromic_subsequence(s: str) -> int:
        ar = [[] for _ in range(26)]
        for i in range(len(s)):
            ar[ord(s[i]) - ord('a')].append(i)

        answer = 0
        for c in range(26):
            if not ar[c]:
                continue
            l, r = ar[c][0], ar[c][-1]
            if r - l < 2:
                continue
            for m in range(26):
                if bisect_right(ar[m], l) != bisect_left(ar[m], r):
                    answer += 1
        return answer
