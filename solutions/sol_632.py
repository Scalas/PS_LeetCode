from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def smallest_range(nums: List[List[int]]) -> List[int]:
        k = len(nums)
        lines: dict[int, List[int]] = defaultdict(list)
        for i in range(k):
            for num in nums[i]:
                lines[num].append(i)
        ns = sorted(set([nums[i][j] for i in range(k) for j in range(len(nums[i]))]))
        n = len(ns)
        count = [0] * k
        lc = 0

        def inc(li):
            nonlocal count, lc
            if count[li] == 0:
                lc += 1
            count[li] += 1

        def dec(li):
            nonlocal count, lc
            if count[li] == 1:
                lc -= 1
            count[li] -= 1

        s = 0
        md, ms, me = ns[-1] - ns[0] + 1, ns[0], ns[-1]
        for e in range(n):
            for i in lines[ns[e]]:
                inc(i)
            if lc < k:
                continue
            while lc == k:
                diff = ns[e] - ns[s] + 1
                if diff < md:
                    md, ms, me = diff, ns[s], ns[e]
                for j in lines[ns[s]]:
                    dec(j)
                s += 1
        return [ms, me]
