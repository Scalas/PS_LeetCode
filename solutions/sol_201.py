class Solution:
    @staticmethod
    def range_bitwise_and(left: int, right: int) -> int:
        base = left
        maxv = right
        digit = 1
        answer = 0
        while base:
            bit = base % 2
            if bit and base + 1 > maxv:
                answer += digit
            digit *= 2
            base //= 2
            maxv //= 2
        return answer
