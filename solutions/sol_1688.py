class Solution:
    @staticmethod
    def number_of_matches(n: int) -> int:
        answer = 0
        while n > 1:
            answer += n // 2
            n = n // 2 + n % 2
        return answer
