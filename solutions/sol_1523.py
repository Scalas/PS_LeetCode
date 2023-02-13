class Solution:
    @staticmethod
    def count_odds(low: int, high: int) -> int:
        return (high + 1) // 2 - (low + 1) // 2 + low % 2
