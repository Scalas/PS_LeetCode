from typing import List


class Solution:
    @staticmethod
    def can_traverse_all_pairs(nums: List[int]) -> bool:
        if nums.count(1) > 1:
            return False
        nums = list(set(nums))
        n = len(nums)
        m = max(nums)
        is_prime = [True for _ in range(m + 1)]
        is_prime[0] = is_prime[1] = False

        def union(u, a, b):
            a = find(u, a)
            b = find(u, b)
            if a != b:
                if u[a] < u[b]:
                    u[a] += u[b]
                    u[b] = a
                else:
                    u[b] += u[a]
                    u[a] = b

        def find(u, x):
            if u[x] < 0:
                return x
            u[x] = find(u, u[x])
            return u[x]

        us = [-1] * n
        index = dict()
        for i in range(n):
            index[nums[i]] = i
        for i in range(2, m + 1):
            if not is_prime[i]:
                continue
            group = []
            if i in index:
                group.append(index[i])
            for j in range(i * 2, m + 1, i):
                is_prime[j] = False
                idx = index.get(j, -1)
                if idx != -1:
                    group.append(idx)
            for j in range(len(group) - 1):
                union(us, group[j], group[j + 1])
        return len([p for p in us if p < 0]) == 1
