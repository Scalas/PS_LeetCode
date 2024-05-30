class Solution:
    @staticmethod
    def num_steps(s: str) -> int:
        num = int(s, 2)
        answer = 0
        while num > 1:
            if num % 2:
                num += 1
                answer += 1
            num //= 2
            answer += 1
        return answer
