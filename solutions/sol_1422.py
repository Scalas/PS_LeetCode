class Solution:
    @staticmethod
    def max_score(s: str) -> int:
        l, r = s[0].count("0"), s[1:].count("1")
        answer = l + r
        for c in s[1:-1]:
            if c == "0":
                l += 1
            else:
                r -= 1
            answer = max(answer, l + r)
        return answer
