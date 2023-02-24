from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def minimum_deviation(nums: List[int]) -> int:
        cands = set()
        cands_id = defaultdict(set)
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num % 2:
                cands.add(num)
                cands_id[num].add(i)
                cands.add(num * 2)
                cands_id[num * 2].add(i)
            else:
                while not num % 2:
                    cands.add(num)
                    cands_id[num].add(i)
                    num //= 2
                cands.add(num)
                cands_id[num].add(i)
        cands = sorted(cands)
        id_count = defaultdict(int)
        count = 0
        s, e = 0, 0
        m = len(cands)
        answer = float('inf')
        while e < m:
            for i in cands_id[cands[e]]:
                if not id_count[i]:
                    count += 1
                id_count[i] += 1
            while count == n:
                answer = min(answer, cands[e] - cands[s])
                for i in cands_id[cands[s]]:
                    id_count[i] -= 1
                    if not id_count[i]:
                        count -= 1
                s += 1
            e += 1

        return answer
