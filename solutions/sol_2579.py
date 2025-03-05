class Solution:
    @staticmethod
    def colored_cells(n: int) -> int:
        return n * (n - 1) * 2 + 1
