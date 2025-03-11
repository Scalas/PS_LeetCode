class Solution:
    @staticmethod
    def number_of_substrings(s: str) -> int:
        n = len(s)
        count = [0] * 3

        def index(char):
            if char == "a":
                return 0
            if char == "b":
                return 1
            else:
                return 2

        answer = 0
        start = 0
        for i in range(n):
            c = s[i]
            count[index(c)] += 1
            if min(count) == 0:
                continue
            r = n - i
            while min(count) > 0:
                answer += r
                count[index(s[start])] -= 1
                start += 1
        return answer
