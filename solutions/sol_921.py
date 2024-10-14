class Solution:
    @staticmethod
    def min_add_to_make_valid(s: str) -> int:
        p = 0
        answer = 0
        for c in s:
            if c == "(":
                p += 1
            else:
                if p:
                    p -= 1
                else:
                    answer += 1
        answer += p
        return answer
