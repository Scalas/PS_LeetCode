class Solution:
    @staticmethod
    def judge_square_sum(c: int) -> bool:
        for i in range(int(c**0.5) + 1):
            r = c - i**2
            if r**0.5 == int(r**0.5):
                return True
        return False
