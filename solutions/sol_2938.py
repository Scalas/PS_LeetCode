class Solution:
    @staticmethod
    def minimum_steps(s: str) -> int:
        answer = 0
        idx = 0
        for i in range(len(s)):
            if s[i] == "1":
                continue
            answer += i - idx
            idx += 1
        return answer
