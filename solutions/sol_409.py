from collections import defaultdict


class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> int:
        count = defaultdict(int)
        answer = 0
        for c in s:
            count[c] += 1
            if count[c] == 2:
                count[c] = 0
                answer += 2
        if answer < len(s):
            answer += 1
        return answer
