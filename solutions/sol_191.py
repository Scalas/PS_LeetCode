class Solution:
    @staticmethod
    def hamming_weight(n: int) -> int:
        answer = 0
        while n:
            answer += n % 2
            n //= 2
        return answer
