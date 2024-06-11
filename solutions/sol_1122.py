from typing import List


class Solution:
    @staticmethod
    def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
        idx = dict()
        for i in range(len(arr2)):
            idx[arr2[i]] = i
        return sorted(arr1, key=lambda x: (idx.get(x, 1001), x))
