from typing import List


class Solution:
    @staticmethod
    def matrix_score(grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def to_num(arr):
            val = 0
            r = 1
            for idx in range(len(arr) - 1, -1, -1):
                val += arr[idx] * r
                r *= 2
            return val

        def xor_bit(o1, offset):
            t = (o1 & offset)
            if o1 & offset:
                return o1 - offset
            return o1 + offset

        for i in range(n):
            rev = [1 - x for x in grid[i]]
            num_b = to_num(grid[i])
            num_a = to_num(rev)
            if num_a > num_b:
                grid[i] = rev

        nums = [to_num(grid[i]) for i in range(n)]
        s = sum(nums)

        for i in range(m):
            d = 1 << i
            res = []
            for num in nums:
                res.append(xor_bit(num, d))
            ns = sum(res)
            if ns > s:
                nums = res
                s = ns
        return s
