from typing import List


class Solution:
    @staticmethod
    def search_matrix(matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        s, e = 0, n * m - 1
        while s <= e:
            mid = (s + e) // 2
            r, c = mid // m, mid % m
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                s = mid + 1
            else:
                e = mid - 1
        return False
