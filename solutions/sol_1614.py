class Solution:
    @staticmethod
    def max_depth(s: str) -> int:
        answer = 0
        cur = 0
        for c in s:
            if c == "(":
                cur += 1
                answer = max(answer, cur)
            elif c == ")":
                cur -= 1
        return answer
