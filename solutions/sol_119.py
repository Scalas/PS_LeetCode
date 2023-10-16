from typing import List


class Solution:
    @staticmethod
    def get_row(row_index: int) -> List[int]:
        row = [1]
        for _ in range(row_index):
            nrow = [1] * (len(row) + 1)
            for i in range(1, len(row)):
                nrow[i] = row[i - 1] + row[i]
            row = nrow
        return row
