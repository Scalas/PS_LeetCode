from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def sub_arrays_with_k_distinct(nums: List[int], k: int) -> int:
        def x_diff(x: int, arr: List[int]):
            n = len(arr)
            arr = arr + [0]
            count = defaultdict(int)
            e = 0
            nc = 0
            res = []
            for s in range(n):
                count[arr[s - 1]] -= 1
                if count[arr[s - 1]] == 0:
                    nc -= 1
                if nc == x:
                    res.append(e - 1)
                    continue
                while e < n:
                    count[arr[e]] += 1
                    if count[arr[e]] == 1:
                        nc += 1
                        if nc == x:
                            e += 1
                            break
                    e += 1
                res.append(e - 1 if nc == x else n)
            return res

        return sum([v - u for u, v in zip(x_diff(k, nums), x_diff(k + 1, nums))])
