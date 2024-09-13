class Solution:
    @staticmethod
    def min_bit_flips(start: int, goal: int) -> int:
        xor = (~start & goal) | (start & ~goal)
        answer = 0
        while xor:
            answer += xor % 2
            xor //= 2
        return answer
