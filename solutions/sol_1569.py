from typing import List


class Solution:
    @staticmethod
    def num_of_ways(nums: List[int]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7

        # build BST
        root = nums[0]
        g = [[-1, -1] for _ in range(n + 1)]
        for num in nums[1:]:
            p = root
            idx = 0 if num < p else 1
            while g[p][idx] != -1:
                p = g[p][idx]
                idx = 0 if num < p else 1
            g[p][idx] = num

        def order(cur, begin, end):
            idx = cur - 1
            if g[cur][0] == g[cur][1] == -1:
                return 1
            if g[cur][1] == -1:
                return order(g[cur][0], begin, idx - 1)
            if g[cur][0] == -1:
                return order(g[cur][1], idx + 1, end)
            left = idx - begin
            right = end - idx
            return (dup_comb(left + 1, right) * order(g[cur][0], begin, idx - 1) * order(g[cur][1], idx + 1, end)) % mod

        def dup_comb(x, y):
            res = 1
            for i in range(x + y - 1, x - 1, -1):
                res *= i
            for i in range(1, y + 1):
                res //= i
            return res

        return order(root, 0, n - 1) - 1
