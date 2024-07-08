class Solution:
    @staticmethod
    def pass_the_pillow(n: int, time: int) -> int:
        r = time % (n * 2 - 2) + 1
        if r > n:
            return n * 2 - r
        return r
