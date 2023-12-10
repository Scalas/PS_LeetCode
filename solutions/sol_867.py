from typing import List


class Solution:
    @staticmethod
    def transpose(matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))
