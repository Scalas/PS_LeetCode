from typing import List


class Solution:
    @staticmethod
    def peak_index_in_mountain_array(arr: List[int]) -> int:
        n = len(arr)

        def check(idx):
            if idx > 0 and arr[idx] < arr[idx - 1]:
                return 1
            if idx < n - 1 and arr[idx] < arr[idx + 1]:
                return -1
            return 0

        s, e = 0, n - 1
        while s <= e:
            m = (s + e) // 2
            c = check(m)
            if c < 0:
                s = m + 1
            elif c > 0:
                e = m - 1
            else:
                return m
